import cv2
import numpy as np
import tensorflow as tf
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions


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
    frame = cv2.resize(frame,(224,224))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Inversement caneaux couleurs BGR (base de opencv) à RGB
    frame_array = img_array = np.expand_dims(frame_rgb, axis=0) # Convertir en batch avec une image par batch 
    img_preprocessed = preprocess_input(frame_array) # COnvertissage en float et normalisation des pixels : (255,0,0) devient (-1,1,1) pour MobilNet entre -1 et 1
    predictions = model.predict(img_preprocessed)
    best_pred = decode_predictions(predictions,top=1)[0]
    label = f"{best_pred[0][1]} : {best_pred[0][2]*100:.1f}%"
    cv2.putText(frame, label, (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2)

    cv2.imshow("Caméra",frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
