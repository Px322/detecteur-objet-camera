import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    for box in results.boxes:
        label = model.names[int(box.cls[0])]
        if label == "person":  # détection
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        score = float(box.conf[0]) * 100
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {score:.1f}%", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("YOLO", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
