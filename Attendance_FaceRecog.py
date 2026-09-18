import cv2 # library for computer vision tasks
import numpy as np # library for numerical computations
import face_recognition # Face recognition library
import os # library for file and directory operations
from datetime import datetime # library for working with dates and times

# Path to the directory containing registered images
path = 'Faces'
# list to store the attendance images
images = []
# list to store the class names
classNames = []
# get the list of files in the registered image directory
myList = os.listdir(path)
print(myList)
for cl in myList:
    # for read each attendance image
    curImg = cv2.imread(f'{path}/{cl}')
    # Append the image to the images list
    images.append(curImg)
    # Append the class name to the classNames list
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        # Convert image from BGR to RGB format
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # Encode the face in the image
        encode = face_recognition.face_encodings(img)[0]
        # Append the face encoding to the encodeList
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    # Open the attendance CSV file for reading and writing
    with open('Attendance.csv', 'r+') as f:
        # Read all lines from the file
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            # Split each line by comma
            entry = line.split(',')
            # Append the name to the nameList
            nameList.append(entry[0])
        # Check if the name is not already in the attendance list
        if name not in nameList:
            now = datetime.now()
            # Get the current time as a string
            dtString = now.strftime('%H:%M:%S')
            # Write the name and time to the file
            f.writelines(f'\n{name},{dtString}')


# Get the face encodings for the attendance images
encodeListKnown = findEncodings(images)
# for checking
print('Encoding Complete')
# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    success, img = cap.read()
    # Resize the frame
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    # for convert the frame from BGR to RGB format
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Locate faces in the current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    # Encode the faces in the current frame
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        # Compare the face with known encodings
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        # Calculate the face distance
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        # Find the index of the best match
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            # Get the name corresponding to the best match
            name = classNames[matchIndex].upper()
            # Get the face coordinates
            y1, x2, y2, x1 = faceLoc
            # Scale the coordinates
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # Draw a rectangle shape around the face
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw a filled rectangle for name
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            # adding text for name
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # Mark the attendance for the recognized person
            markAttendance(name)

# To find the unknown faces we will replace with this

# From here all this does is to check if the distance to our min face is less than 0.5 or not.
# If its not then this means the person is unknown so, we change the name to unknown and don’t mark the attendance.

        if faceDis[matchIndex] < 0.50:
            name = classNames[matchIndex].upper()
            markAttendance(name)
        else:
            name = '!Unknown!'

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # Display the image with the recognized faces in a window titled 'Face Scan'
    cv2.imshow('Face Scan', img)
    # Wait for a key press for 1 millisecond ( this allows the image to be displayed)
    cv2.waitKey(1)