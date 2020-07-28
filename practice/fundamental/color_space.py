# color_space.py

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# cv2.addText(image, "This is Mukesh", 20, ('Times'))
cv2.imshow("image", image)
cv2.imshow("HSV", hsv)
cv2.imshow("gray", gray)
cv2.imshow("lab", lab)
cv2.waitKey(0)
