import numpy as np
import cv2

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_classifier.detectMultiScale(gray, 1.3, 5)
    print(face)
    if face is not ():
        (x, y, w, z) = tuple(face[0])
        cv2.rectangle(frame, (x, x + w), (y, y + z), (0, 255, 0), 2)
        cv2.putText(frame, "Face Found", (250, 450),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Image", frame)
    else:
        cv2.putText(frame, "NO Face Found", (250, 450),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Image", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
