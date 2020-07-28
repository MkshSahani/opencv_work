# gaussian_blur.py


import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="PATH OF IMAGE")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])

blurred = np.hstack([cv2.GaussianBlur(image, (3, 3), 0), cv2.GaussianBlur(
    image, (5, 5), 0), cv2.GaussianBlur(image, (5,  5), 0)])

cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
