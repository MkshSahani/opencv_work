# translation.py
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Source to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
cv2.imshow("Original Image", image)
# cv2.waitKey(0)
M = np.float32([[1, 0, 50], [0, 1, 20]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Translated Image", shifted)

M = np.float32([[1, 0, -50], [0, 1, -80]])
shifted2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Translated Image2", shifted2)
cv2.waitKey(0)
