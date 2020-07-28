# split_marge.py

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
(B, G, R) = cv2.split(image)
cv2.imshow("blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.imshow("Image", cv2.merge([B, G, R]))
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
