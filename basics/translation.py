import numpy as np
import argparse
import cv2
# import imutils

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path To Image")
    args = vars(ap.parse_args())
    image = cv2.imread(args['image'])
    cv2.imshow("Original", image)
    cv2.waitKey(0)
    M = np.float32([[1, 0, 25], [0, 1, 50]])
    