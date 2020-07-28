import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
cv2.imshow("Original Image", image)
cv2.imshow("Shifted Image", imutils.translate(image, 0, 100))
cv2.waitKey(0)
