# drawing.py

# import argparse
import numpy as np
import cv2

if __name__ == '__main__':
    # main function
    # arg = argparse.ArgumentParser()
    # arg.add_argument("-i", "--image", required=True,
    #                  help="For the Link of Image")
    # args = vars(arg.parse_args())
    # print(args)
    green = (0, 255, 0)
    red = (0, 0, 255)
    blue = (255, 0, 0)
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    # cv2.imshow("Canvas", canvas)
    cv2.line(canvas, (0, 0), (300, 300), green)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.line(canvas, (0, 300), (300, 0), red, 3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.rectangle(canvas, (10, 10), (60, 60), green, 1)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
