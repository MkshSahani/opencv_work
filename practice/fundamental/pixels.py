# learning about the pixel of image.
# as i know the pixel is the buidling block of the image.
# A image is a matrix of the pixels.

import numpy as np
import cv2
import matplotlib.pyplot as plt
image = np.random.randint(0, high=255, size=(400, 400, 3), dtype="uint8")
cv2.imshow("RANDOM_IMAGE", image)
image2 = image[100:200, 200:300]
cv2.imshow("CROPPED IMAGE", image2)
image3 = np.random.randint(0, high=255, size=(400, 400, 1), dtype="uint8")
cv2.imshow("BLACK_WHITE_IMAGE", image3)
data = cv2.calcHist([image], [0], None, [256], [00, 256])
plt.plot(data)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
