import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args['image'])
image = cv2.resize(image, (500, 500))
cv2.imshow("Image", image)
cv2.imwrite("coins_image.jpg", image)
cv2.waitKey(0)
