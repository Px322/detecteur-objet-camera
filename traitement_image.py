import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.applications.MobileNetV2(weights="imagenet")
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not capture.isOpened():
    print("Impossible d'ouvrir la caméra")
    exit()


