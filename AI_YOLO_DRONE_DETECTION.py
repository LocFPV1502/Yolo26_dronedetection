import cv2
import time
import numpy as np
from ultralytics import YOLO


MODEL_PATH = "weights/best.pt"
CAMERA_INDEX = 0
CONF_THRES = 0.25


def draw_label(img, text, x, y):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    thickness = 2

    (text_w, text_h), baseline = cv2.getTextSize(text, font, font_scale, thickness)

    if y - text_h - 10 < 0:
        y = y + text_h + 10

    cv2.rectangle(
        img,
        (x, y - text_h - 10),
        (x + text_w + 10, y),
        (0, 255, 0),
        -1
    )

    cv2.putText(
        img,
        text,
        (x + 5, y - 5),
        font,
        font_scale,
        (0, 0, 0),
        thickness
    )


def main():
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print(f"Khong the mo camera {CAMERA_INDEX}")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    prev_time = time.time()

    cv2.namedWindow("Drone Detection", cv2.WINDOW_NORMAL)

    print("Nhan phim 'q' de thoat.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Khong doc duoc frame tu camera")
            break

        original_frame = frame.copy()
        detected_frame = frame.copy()

        results = model(frame, conf=CONF_THRES, verbose=False)

        for result in results:
            boxes = result.boxes
            if boxes is None:
                continue

            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0]) if box.conf is not None else 0.0

                cv2.rectangle(detected_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                draw_label(detected_frame, f"Phat hien drone: {conf:.2f}", x1, y1)

        current_time = time.time()
        fps = 1.0 / (current_time - prev_time) if current_time != prev_time else 0.0
        prev_time = current_time

        fps_text = f"FPS: {fps:.2f}"

        cv2.putText(
            original_frame,
            fps_text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.putText(
            detected_frame,
            fps_text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.putText(
            original_frame,
            "Chua detect",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            detected_frame,
            "Sau detect",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        combined_frame = np.hstack((original_frame, detected_frame))

        cv2.imshow("Drone Detection", combined_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
