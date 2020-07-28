# in this section we will learn how to draw the shapes on the image.

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To image")
args = vars(ap.parse_args())
print(args)

canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.line(canvas, (0, 0), (400, 400), (0, 255, 0), 5)
cv2.line(canvas, (400, 0), (0, 400), (0, 255, 0), 5)
cv2.circle(canvas, (200, 200), 200, (0, 0, 255), -1)
cv2.rectangle(canvas, (50, 50), (350, 350), (255, 0, 0), -1)
cv2.imshow("CANVAS", canvas)
cv2.waitKey(0)
