# arithmetic.py
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
cv2.imshow("Original  Image", image)
print(f"Max of 255 {cv2.add(np.uint8([200]), np.uint8([100]))}")
print(f"Min of 0 {cv2.subtract(np.uint8([50]), np.uint8([100]))}")
print(f"Wrap around {np.uint8([200]) + np.uint8([100])}")
print(f"Wrap around {np.uint8([50]) - np.uint8([100])}")

# added image.
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("added", added)
M = np.ones(image.shape, dtype="uint8") * 50
subtract = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtract)
cv2.waitKey(0)
