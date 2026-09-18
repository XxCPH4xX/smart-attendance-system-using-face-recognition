# Smart Attendance System Using Face Recognition

An AI-powered attendance management system that automates attendance tracking using real-time face recognition technology. The system detects and identifies registered students through a webcam and automatically records their attendance with timestamps.

## Features

- **Real-Time Face Detection**: Detects faces in live webcam feed using OpenCV
- **Face Recognition**: Identifies registered students using the `face_recognition` library
- **Automatic Attendance Marking**: Records attendance with timestamps in CSV format
- **Visual Feedback**: Displays green bounding boxes and names on recognized faces
- **Unknown Face Detection**: Identifies and labels unrecognized individuals
- **Simple Registration**: Add new users by placing face images in the `Faces/` folder

## Demo

1. System启动后自动打开摄像头
2. 检测到已注册的人脸时，显示绿色边框和姓名
3. 自动将出勤记录写入 `Attendance.csv`

## Project Structure

```
smart-attendance-system-using-face-recognition/
├── Faces/                    # Directory containing registered face images
│   ├── Fahim.jpg
│   ├── Hritik.jpg
│   ├── Imtiaz.jpg
│   └── Taylor Swift.jpg
├── Attendance.csv            # Attendance records (auto-generated)
├── Attendance_FaceRecog.py   # Main application script
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## Requirements

- Python 3.7 or higher
- Webcam (built-in or external)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/XxCPH4xX/smart-attendance-system-using-face-recognition.git
cd smart-attendance-system-using-face-recognition
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install dlib (if face_recognition installation fails)

```bash
# Windows
pip install dlib

# macOS
brew install cmake
pip install dlib
```

## Usage

### 1. Register New Users

Place face images in the `Faces/` directory:
- Image filename becomes the person's name (e.g., `John_Doe.jpg`)
- Use clear, front-facing photos with good lighting
- Supported formats: JPG, JPEG, PNG

### 2. Run the System

```bash
python Attendance_FaceRecog.py
```

### 3. How It Works

1. The webcam opens automatically
2. Position yourself or others in front of the camera
3. The system will:
   - Detect faces in real-time
   - Compare with registered faces
   - Display green bounding box and name for recognized faces
   - Mark attendance in `Attendance.csv` with timestamp

### 4. View Attendance

```bash
# Open in Excel
start Attendance.csv

# Or view in terminal
cat Attendance.csv
```

## Attendance Format

The `Attendance.csv` file stores records in the following format:

```
Name,Time
FAHIM,14:30:25
HRITIK,14:31:02
```

## Configuration

### Adjusting Recognition Sensitivity

In `Attendance_FaceRecog.py`, you can modify the face distance threshold:

```python
# Lower value = stricter matching (fewer false positives)
# Higher value = more lenient matching (fewer false negatives)
if faceDis[matchIndex] < 0.50:  # Default threshold
    name = classNames[matchIndex].upper()
    markAttendance(name)
else:
    name = '!Unknown!'
```

### Changing Camera Index

```python
# Use 0 for default webcam, 1 for external camera
cap = cv2.VideoCapture(0)
```

## Technologies Used

| Technology | Description |
|------------|-------------|
| Python | Core programming language |
| OpenCV | Computer vision and image processing |
| face_recognition | Face detection and recognition |
| NumPy | Numerical computations |
| datetime | Timestamp generation |

## How Face Recognition Works

1. **Encoding Phase**: The system reads all images from `Faces/` folder and creates 128-dimensional face encodings
2. **Detection Phase**: Webcam frames are resized and processed to detect face locations
3. **Matching Phase**: Detected faces are compared with known encodings using Euclidean distance
4. **Decision Phase**: If distance < 0.50, the face is recognized; otherwise, it's marked as unknown

## Troubleshooting

### Common Issues

1. **"No module named 'face_recognition'"**
   ```bash
   pip install face_recognition
   ```

2. **"Could not import dlib"**
   ```bash
   pip install dlib
   ```

3. **Webcam not working**
   - Check if another application is using the camera
   - Try changing camera index: `cv2.VideoCapture(1)`

4. **Poor recognition accuracy**
   - Use high-quality, well-lit face images
   - Ensure faces are clearly visible and front-facing
   - Adjust the threshold value in the code

## Future Enhancements

- [ ] Add database integration (SQLite/MySQL)
- [ ] Create a web-based dashboard
- [ ] Add student registration via webcam
- [ ] Implement attendance reports and analytics
- [ ] Add email/SMS notifications
- [ ] Support multiple camera angles
- [ ] Add anti-spoofing measures

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**XxCPH4xX** - [GitHub Profile](https://github.com/XxCPH4xX)

## Acknowledgments

- [face_recognition](https://github.com/ageitgey/face_recognition) - Simple face recognition library
- [OpenCV](https://opencv.org/) - Open source computer vision library
- [dlib](http://dlib.net/) - Modern C++ toolkit containing machine learning algorithms
