# color histogram
import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
# command line argument.

image = cv2.imread(args['image'])
colors = ("b", "g", "r")
chans = cv2.split(image)
# now you have the channels.
plt.figure()
plt.title("Colored Picture Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for (color, chan) in zip(colors, chans):
    data = cv2.calcHist([chan], [0], None, [256], [0, 255])
    plt.plot(data)
    plt.xlim([0, 256])

plt.show()
