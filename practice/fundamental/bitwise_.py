import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To image")
args = vars(ap.parse_args())
print(args)

rectangle = np.zeros((500, 500, 1), dtype="uint8")
cv2.rectangle(rectangle, (50, 50), (450, 450), 255, -1)
cv2.imshow("Rectangle", rectangle)
circle = np.zeros((500, 500, 1), dtype="uint8")
cv2.circle(circle, (250, 250), 250, 255, -1)
cv2.imshow("Circle", circle)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("BIT_WISE_OR", bitwiseOr)
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("BIT_WISE_AND", bitwiseAnd)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("BIT_WISE_XOR", bitwiseXor)
cv2.waitKey(0)
