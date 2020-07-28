# median_blur.py

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="PATH OF IMAGE")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])

blurred = np.hstack([cv2.medianBlur(image, 3), cv2.medianBlur(
    image, 5), cv2.medianBlur(image, 7)])


cv2.imshow("Blurred.", blurred)

cv2.imshow("Image", image)
cv2.waitKey(0)
