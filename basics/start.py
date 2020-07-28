import numpy as np
import cv2

data = np.random.randint(0, high=255, size=(500, 500, 3), dtype="uint8")
print(data[0:5, 0:5])
cv2.imshow("Image", data)
cv2.waitKey(0)
