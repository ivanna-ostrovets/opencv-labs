import cv2
import numpy as np


def lab_11_morphological(filename):
    # Morphological Transformations
    image = cv2.imread(filename, 0)
    cv2.imshow("image1", image)

    # Erosion
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    cv2.imshow("erosion", erosion)

    # Dilation
    dilation = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow("dilation", dilation)

    # Opening
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow("opening", opening)

    # Closing
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("closing", closing)

    # Smoothing Filters
    # Median Blurring
    slides_number = 100

    for number in range(1, slides_number + 1):
        median = cv2.medianBlur(image, number if number % 2 != 0 else number + 1)
        cv2.imwrite(f"lab_11_slides/image{number}.bmp", median)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
