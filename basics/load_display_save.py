import argparse
import cv2


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the Image")
    args = vars(ap.parse_args())
    print(args)
    image = cv2.imread(args['image'])
    print(f"With : {image.shape[0]}")
    print(f"Height : {image.shape[1]}")
    b, g, r = image[0, 0]
    print(f"Red : {r} Green : {g} : Blue : {b}")
    image[0, 0] = (0, 0, 255)
    b, g, r = image[0, 0]
    print(f"Red : {r} Green : {g} : Blue : {b}")
    cv2.imshow("Image", image)

    cv2.waitKey(0)
    # cv2.imwrite("filename.format", image)
