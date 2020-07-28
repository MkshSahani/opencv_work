# following are the acitivities in this practical
# 1. video capturing.
import cv2

cameraCapture = cv2.VideoCapture(0)

success, frame = cameraCapture.read()
print(success)
while success and cv2.waitKey(0) == True:
    cv2.imshow("Image", frame)
    success, frame = cameraCapture.read()
    print(success)

cameraCapture.release()
cv2.waitKey(0)
