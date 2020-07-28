# this script is for testing purpose.
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
# cv2.imshow("Original  Image", image)
res = cv2.resize(image, (600, 600))
cv2.imshow("Lets see", res)
name = input("Picture Name : ")
if name != "":
    cv2.imwrite(name, res)
cv2.waitKey(0)
