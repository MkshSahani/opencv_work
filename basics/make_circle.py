# making circle

import cv2
import numpy as np

if __name__ == '__main__':
    # canvas where you will apply everything.
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    # centerX and centerY is the center of the canvas.
    (centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
    # white color.
    white = (255, 255, 255)
    for i in range(0, 100, 5):
        cv2.circle(canvas, (centerX, centerY), i, white)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
