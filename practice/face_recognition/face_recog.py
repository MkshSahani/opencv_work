import numpy as np 
import cv2 
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args['image'])
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray_ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = face_classifier.detectMultiScale(gray_, 1.3, 5)
print(face == ())
print(face)


