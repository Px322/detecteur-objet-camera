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
    frame = cv2.resize(frame,(224,224))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Inversement caneaux couleurs BGR (base de opencv) à RGB
    frame_array = img_array = np.expand_dims(frame, axis=0)
    img_preprocessed = tf.preprocess_input(frame_array)
    predictions = model.predict(img_preprocessed)

    if not ret:
        print("Impossible de recevoir les frames de la vidéo")
        break
    cv2.imshow("Caméra",frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
