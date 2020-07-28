import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

(T, thresed_image) = cv2.threshold(image, 155, 255, cv2.THRESH_BINARY)
(T, inveresed_thresed_image) = cv2.threshold(
    image, 155, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Threased Image", thresed_image)
cv2.imshow("Inveresed Threased Image", inveresed_thresed_image)

cv2.imshow("Coins", cv2.bitwise_or(image, image, mask=inveresed_thresed_image))


cv2.waitKey(0)
