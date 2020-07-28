import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
# command line argument
image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
data = cv2.calcHist([image], [0], None, [256], [0, 255])

plt.figure()
plt.title("Histgram of Gray Scale")
plt.xlabel("Bins")
plt.ylabel("# Number of pixels")
plt.xlim([0, 256])
plt.plot(data)
plt.show()
