import argparse
import cv2

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--image", required=True, help="Path To image")
    args = vars(arg.parse_args())
    print(args)
    image = cv2.imread(args['image'])
    corner = image[50:120, 50:150]
    cv2.imshow("Corner", corner)
    image[50:120, 50:150] = (0, 255, 0)

    cv2.imshow("Image", image)
    print(f"Height  {image.shape[1]} Width : {image.shape[0]}")
    cv2.waitKey(0)
