# test.py

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])
cv2.imshow("Image", image)
# (b, g, r) = cv2.split(image)
# # image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # image2 = np.transpose(image2)
# b = b[::-1]
# g = g[::-1]
# r = r[::-1]


# cv2.imshow("Transponse", cv2.merge([b, g, r]))
image2 = image[::-1]
cv2.imshow("transpose", image2)

cv2.waitKey(0)
