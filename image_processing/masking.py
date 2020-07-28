# masking.py
import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
cv2.imshow("Original Image", image)
mask = np.zeros(image.shape[:2], dtype="uint8")
cx, cy = image.shape[1] // 2, image.shape[0] // 2
cv2.rectangle(mask, (cx - 100, cy - 100), (cx + 100, cy + 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)


cv2.waitKey(0)
