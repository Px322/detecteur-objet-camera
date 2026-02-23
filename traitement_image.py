import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.applications.MobileNetV2(weights="imagenet")
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not capture.isOpened():
    print("Impossible d'ouvrir la caméra")
    exit()
while True:
    ret, frame = capture.read()

    if not ret:
        print("Impossible de recevoir les frames de la vidéo")
        break
    cv2.imshow("Caméra",frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
