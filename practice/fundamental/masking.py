# for learning about the masking.

import argparse
import numpy as np
import cv2

# argument parser.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to Image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])
# get the shape of the image.
print(image.shape)

mask = np.zeros(image.shape[:2], dtype="uint8")
(cx, cy) = image.shape[0] // 2, image.shape[1] // 2
cv2.rectangle(mask, (cx - 50, cy - 50), (cx + 50, cy + 50), 255, -1)

masked_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Maskked Image", masked_image)
cv2.waitKey(0)
