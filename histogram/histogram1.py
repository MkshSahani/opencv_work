# histogram1.py

import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist(image, [0], None, [256], [0, 256])

plt.figure()
plt.title("GRAPH HISTOGRAM.")
plt.xlabel("bins")
plt.ylabel("# of pixel")
plt.plot(hist)
plt.xlim([0, 256])

cv2.imshow("GRAYSCALE IMAGE", image)
plt.show()

cv2.waitKey(0)
