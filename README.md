# Real-Time Drone Detection with YOLO and OpenCV

This project performs **real-time drone detection from a webcam feed** using a trained **Ultralytics YOLO** model and displays the results side by side:

- **Left panel:** original camera frame
- **Right panel:** detection result with bounding boxes, confidence scores, and FPS

The script loads a custom model from `weights/best.pt`, captures video from the default camera, runs inference on each frame, and shows the processed output in a desktop window. fileciteturn0file0

---

## Features

- Real-time object detection from a live camera
- Custom YOLO model support
- Bounding box and confidence label rendering
- FPS display for performance monitoring
- Side-by-side comparison between raw and detected frames
- Simple keyboard exit with `q` fileciteturn0file0

---

## Project Structure

```text
project/
├── main.py                # your Python script
└── weights/
    └── best.pt            # trained YOLO model weights
```

> If your script has a different filename, replace `main.py` in the commands below with your actual filename.

---

## Requirements

- Python 3.9+
- A working webcam
- A trained YOLO model at `weights/best.pt`

Python libraries used by the script:

- `opencv-python`
- `numpy`
- `ultralytics` fileciteturn0file0

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Create and activate a virtual environment (recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install opencv-python numpy ultralytics
```

---

## Model Setup

Place your trained YOLO weight file at:

```text
weights/best.pt
```

The script uses this path by default through the constant below:

```python
MODEL_PATH = "weights/best.pt"
```

If your model is stored elsewhere, update the `MODEL_PATH` value inside the script. fileciteturn0file0

---

## Configuration

The main configurable parameters are defined at the top of the script:

```python
MODEL_PATH = "weights/best.pt"
CAMERA_INDEX = 0
CONF_THRES = 0.25
```

### Meaning of each parameter

- `MODEL_PATH`: path to the trained YOLO model
- `CAMERA_INDEX`: webcam index (`0` is usually the default camera)
- `CONF_THRES`: confidence threshold for detections

You can change these values depending on your hardware and model setup. fileciteturn0file0

---

## Usage

Run the script with:

```bash
python main.py
```

What happens when the script starts:

1. The YOLO model is loaded
2. The webcam is opened
3. Frames are captured continuously
4. The model performs detection on each frame
5. The program draws bounding boxes and confidence labels on detected objects
6. FPS is calculated and displayed on screen
7. Two frames are shown side by side in a window named **Drone Detection** fileciteturn0file0

To quit the application, press:

```text
q
```

---

## Output Display

The application shows a combined window containing:

- **Original frame** labeled as `Chua detect`
- **Processed frame** labeled as `Sau detect`
- FPS text on both sides
- Detection boxes with the label `Phat hien drone: <confidence>` when an object is found fileciteturn0file0

---

## Notes and Important Considerations

### 1. The model file is not included automatically
This project depends on a custom YOLO weight file:

```text
weights/best.pt
```

Without this file, the script will not run successfully. Make sure you provide your trained model before running the project. fileciteturn0file0

### 2. Camera access is required
The script uses OpenCV webcam capture:

```python
cap = cv2.VideoCapture(CAMERA_INDEX)
```

If no camera is available, or if the camera index is incorrect, the application will fail to open the stream. fileciteturn0file0

### 3. This is a desktop-based real-time demo
The script opens an OpenCV display window and is intended for local execution on a machine with GUI support. It may not work properly in headless environments such as some cloud servers or remote terminals.

### 4. Performance depends on hardware
Inference speed and FPS depend on:

- your CPU/GPU
- webcam resolution
- YOLO model size
- system load

The script sets the camera resolution to **1280x720**, which may affect performance on lower-end systems. fileciteturn0file0

### 5. Detection quality depends on your trained model
This repository contains inference code only. Actual detection accuracy depends on the training quality, dataset quality, and the custom `best.pt` model you use.

### 6. Current labels in the UI are written in Vietnamese
Although this README is in English, the on-screen messages inside the script are currently Vietnamese, for example:

- `Khong the mo camera`
- `Nhan phim 'q' de thoat.`
- `Phat hien drone`
- `Chua detect`
- `Sau detect` fileciteturn0file0

If you want a fully English project, you may also want to translate these UI strings in the Python source.

---

## Troubleshooting

### Error: model file not found
Check that this file exists:

```text
weights/best.pt
```

### Error: cannot open camera
Try changing:

```python
CAMERA_INDEX = 0
```

to another index such as `1` or `2`. Also make sure no other application is using the webcam.

### Low FPS
Possible improvements:

- reduce camera resolution
- use a smaller YOLO model
- run on a machine with GPU acceleration
- close other heavy applications

---

## Possible Improvements

If you continue developing this project, useful next steps could include:

- saving detection results to video files
- adding screenshot capture
- logging detections with timestamps
- supporting video files in addition to webcam input
- exporting requirements to `requirements.txt`
- adding command-line arguments for model path, camera index, and confidence threshold

---

## License

Add your preferred license here, for example MIT, Apache-2.0, or a private/internal license depending on how you plan to publish the repository.
