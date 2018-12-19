from math import sqrt

import cv2


def lab_13(filename):
    image = cv2.imread(filename)
    height, width, channels = image.shape

    # Sobel
    sobel_x = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=3)

    gray_x = cv2.cvtColor(sobel_x, cv2.COLOR_BGR2GRAY)
    gray_y = cv2.cvtColor(sobel_y, cv2.COLOR_BGR2GRAY)

    combined = gray_x.copy()

    for y in range(height):
        for x in range(width):
            combined[x][y] = sqrt(gray_x[x][y] ** 2 + gray_y[x][y] ** 2)

    retval, threshold = cv2.threshold(combined, 90, 255, cv2.THRESH_BINARY)

    cv2.imshow("image", image)
    cv2.imshow("sobel_x", gray_x)
    cv2.imshow("sobel_y", gray_y)
    cv2.imshow("combined", combined)
    cv2.imshow("threshold", threshold)
    cv2.imshow("threshold", threshold)

    # Canny
    edges = cv2.Canny(image, 90, 200)
    cv2.imshow("Canny", edges)

    # Contours tracing
    im2, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_img = cv2.drawContours(image, contours, -1, (255, 0, 0))

    cv2.imshow("findContours", im2)
    cv2.imshow("findContours", contours_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
