# adaaptive_threasing.py

import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])
image = cv2.GaussianBlur(image, (5, 5), 0)
threased = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
threased_ = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 15, cv2.THRESH_BINARY_INV, 4)

cv2.imshow("Threased Image", threased)
cv2.imshow("Guassion Threasing Image", threased_)
cv2.imshow("image", image)
cv2.waitKey(0)
