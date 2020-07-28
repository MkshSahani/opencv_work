import numpy as np
import cv2
import time

if __name__ == '__main__':
    canvas = np.zeros((400, 400, 3), dtype="uint8")
    cv2.imshow("Canvas", canvas)
    # cv2.waitKey(0)
    j = 0
    while j < 100:
        for i in range(0, 255):
            radius = np.random.randint(5, high=200)
            color = np.random.randint(0, high=256, size=(3,)).tolist()
            pt = np.random.randint(0, high=400, size=(2,))
            cv2.circle(canvas, tuple(pt), radius, color, -1)
        cv2.imshow("Canvas", canvas)
        time.sleep(0.09)
        cv2.waitKey(13)
        j += 1
