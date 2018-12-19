import cv2


def lab_9(filename):
    image = cv2.imread(filename)
    cv2.imshow(filename, image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
