# video.py

import cv2
# camera for reading purpose.
camera = cv2.VideoCapture(0)

# frame contain the data from image.
success, frame = camera.read()
print(success)
while success:
    cv2.imshow("Camera", frame)
    success, frame = camera.read()
cv2.destroyAllWindows()
frame, success
