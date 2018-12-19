import cv2


def lab_12(filename):
    image = cv2.imread(filename)
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    min_rect_dim = 500
    max_rect_dim = 800

    threshold, thresholded_image = cv2.threshold(grayed, 145, 255, cv2.THRESH_BINARY)

    for y in range(thresholded_image.shape[0]):
        for x in range(thresholded_image.shape[1]):
            value = thresholded_image[y][x]

            if value == 255:
                rect = cv2.floodFill(thresholded_image, None, (x, y), 200)[3]
                x, y, width, height = rect

                if (min_rect_dim <= width <= max_rect_dim
                        and min_rect_dim <= height <= max_rect_dim):
                    x1 = x + width // 2
                    y1 = y + height // 2
                    rad = (width + height) // 4
                    cv2.circle(image, (x1, y1), rad, (255, 0, 255), 2)

    cv2.imshow(filename, image)
    cv2.imshow("Thresholded image", thresholded_image)

    cv2.waitKey(235252)
    # cv2.destroyAllWindows()
