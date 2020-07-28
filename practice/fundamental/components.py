# components.py

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])

(b, g, r) = cv2.split(image)

zeros = np.zeros(image.shape[:2], dtype="uint8")

B = cv2.merge([b, zeros, zeros])
R = cv2.merge([zeros, zeros, r])
G = cv2.merge([zeros, g, zeros])

image[0:100, 0:100] = B[0:100, 0:100]
image[0:100, 100:200] = R[0:100, 100:200]
image[100:200, 0:100] = G[100:200, 0:100]

cv2.imshow("Image", image)
cv2.waitKey(0)
