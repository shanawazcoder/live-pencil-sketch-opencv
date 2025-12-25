Live Pencil Sketch Effect (Python + OpenCV)

A real-time computer vision project that converts live webcam video into a **pencil sketch effect**. The application allows switching between normal camera view and sketch mode using keyboard input.



 Features

- Real-time webcam video processing
- Pencil sketch effect using OpenCV
- Toggle between normal and sketch mode
- Smooth live preview
- Simple and beginner-friendly
- Cross-platform support

---

 Technologies Used

- Python 3.x
- OpenCV (cv2)
- NumPy



 Installation
1. Clone the repository

bash
git clone https://github.com/shanawazcoder/live-pencil-sketch-opencv.git
cd live-pencil-sketch-opencv

2. Install dependencies

pip install opencv-python numpy
Usage
Run the script:
python main.py

Keyboard Controls
Key	Action
S	Toggle Sketch / Normal mode
Q	Quit application

How It Works
Captures live video from webcam

Converts frame to grayscale

Inverts grayscale image

Applies Gaussian blur

Inverts blurred image

Divides grayscale image by inverted blur

Produces a realistic pencil sketch effect

Project Structure
live-pencil-sketch-opencv/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore


Use Cases
Computer vision learning project

Webcam filter applications

Image processing demos

Portfolio project

Fun real-time camera effects

