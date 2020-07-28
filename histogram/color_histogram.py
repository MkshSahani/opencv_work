# color_histogram.py

import argparse
import cv2
import numpy
import matplotlib.pyplot as plt
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.title("Colorfull histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixel")
cv2.imshow("Image", image)
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist(chan, [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
