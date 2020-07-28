import argparse
import numpy as np
import cv2

"""
    Notes : 
    1. opencv view image as the numpy ndarray. 
    2. opecv stores RGB in reverse order that is in BGR. 
"""
# argument parser.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to Image")
args = vars(ap.parse_args())
# Here Image a Ndarray and can be think as the Matrix of pixels.
# think about image as matrices.
# these pixels means a lot to you.
image = cv2.imread(args['image'])
overlap_image = np.random.randint(
    0, high=255, size=(100, 100, 1), dtype="uint8")
cv2.imshow("Orignal Image", image)
print(args)
## overlap_image = np.ones(shape=(100, 100, 3), dtype="uint8")
## overlap_image = overlap_image * 130
image[0:100, 0:100] = overlap_image
image[100:200, 100:200] = overlap_image
image[0:100, 100:200] = (0, 255, 0)
cv2.imshow("overlap Image", overlap_image)
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
