import argparse
import numpy as np
import cv2

# HSV (Hue-Saturation-Value)
# L*a*b
# gray

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
# args
image = cv2.imread(args['image'])
cv2.imshow("BGR_IMAGE", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV_IMAGE", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB_IMAGE", lab)

cv2.waitKey(0)
