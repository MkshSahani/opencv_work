# blurring.py

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="PATH OF IMAGE")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])

blurred = np.hstack([cv2.blur(image, (3, 3)), cv2.blur(
    image, (5, 5)), cv2.blur(image, (7, 7))])

cv2.imshow("Original Image", image)
cv2.imshow("Blured Image 3x3", blurred)
cv2.waitKey(0)
