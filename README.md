# Video Frame Extractor

A simple Python tool to extract frames from multiple videos and save them as `.jpg` images for building computer vision datasets.

## Overview

This project helps automate dataset creation from video sources. It reads a list of input videos, calculates how many frames to extract from each one, samples frames at regular intervals, and saves them into a target output folder.

It is useful for tasks such as:

* Object Detection
* Drone Detection
* Image Classification
* Tracking
* Data Annotation

---

## Features

* Extract frames from multiple videos
* Evenly distribute the target number of images across all videos
* Automatically create the output folder if it does not exist
* Save extracted frames as sequentially numbered `.jpg` files
* Handle short videos by extracting all available frames when needed
* Lightweight and easy to run

---

## Project Structure

```bash
.
├── extract_frames.py
├── README.md
└── requirements.txt
```

> Recommended: rename your current script to `extract_frames.py` for better readability.

---

## Requirements

* Python 3.8+
* OpenCV

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
opencv-python>=4.8.0
```

---

## Usage

Update the input video paths and output folder inside the script:

```python
danh_sach_video = [
    "/home/loc_nguyen/AI_DRONE_DETECTION/data1.mp4",
    "/home/loc_nguyen/AI_DRONE_DETECTION/data2.mp4"
]

thu_muc_luu_anh = "/home/loc_nguyen/AI_DRONE_DETECTION/data_images"
```

Then run:

```bash
python extract_frames.py
```

---

## Example

Extract a total of `1000` frames from all input videos:

```python
extract_frames_from_videos(danh_sach_video, thu_muc_luu_anh, target_total_frames=1000)
```

Generated files will look like:

```bash
dataset_img_0000.jpg
dataset_img_0001.jpg
dataset_img_0002.jpg
...
```

---

## Main Function

```python
extract_frames_from_videos(video_paths, output_folder, target_total_frames=1000)
```

### Parameters

| Parameter             | Type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| `video_paths`         | `list` | List of input video paths                         |
| `output_folder`       | `str`  | Folder where extracted images will be saved       |
| `target_total_frames` | `int`  | Total number of frames to extract from all videos |

---

## How It Works

1. Count the number of input videos
2. Divide the target frame count across videos
3. Open each video with OpenCV
4. Compute the extraction interval
5. Save frames at regular steps
6. Print progress logs in the terminal

---

## Sample Output

```bash
Processing video 1/2: data1.mp4
  -> Total frames: 12000 | Target: ~500 images | Interval: every 24 frames
  -> Completed video 1. Saved 500 images.

Processing video 2/2: data2.mp4
  -> Total frames: 8000 | Target: ~500 images | Interval: every 16 frames
  -> Completed video 2. Saved 500 images.

Done! Successfully extracted 1000 images to: /home/loc_nguyen/AI_DRONE_DETECTION/data_images
```

---

## Use Cases

This project is helpful when you want to:

* Build an image dataset from raw videos
* Prepare images for annotation tools such as CVAT, Roboflow, or LabelImg
* Reduce manual screenshot work
* Sample frames evenly to avoid highly redundant data

---

## Notes

* If a video path is invalid, the script will skip that file and continue
* If a video has fewer frames than requested, all frames will be extracted
* For large extraction jobs, make sure the output directory has enough storage space
* You can adjust `target_total_frames` depending on your dataset needs

---

## Possible Improvements

You can extend this project by adding:

* CLI arguments with `argparse`
* FPS-based frame extraction
* Automatic resize before saving
* Blur or duplicate-frame filtering
* Progress bar support with `tqdm`
* Batch loading videos from a folder instead of hardcoding paths

---

## Author

**Loc Nguyen**

---

## License

This project is licensed under the MIT License.
