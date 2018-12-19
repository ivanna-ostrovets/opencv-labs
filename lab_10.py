import cv2
from matplotlib import pyplot as plt


def lab_10(filename):
    image = cv2.imread(filename, 0)

    # Histogram: manual calculation
    height, width = image.shape
    hist = [0] * 256

    for y in range(height):
        for x in range(width):
            hist[image[y][x]] += 1

    plt.bar(range(256), hist)
    plt.show()

    # Histogram: auto
    plt.hist(image.flatten(), 256, [0, 256], color="r", label="Auto histogram")
    plt.show()

    # Normalization
    normalized = image.copy()
    cv2.normalize(image, normalized, 0, 255, cv2.NORM_MINMAX)

    plt.hist(normalized.flatten(), 256, [0, 256], color="g")
    plt.show()

    # Equalization
    equalized = image.copy()
    cv2.equalizeHist(image, equalized)

    plt.hist(equalized.flatten(), 256, [0, 256], color="y")
    plt.show()

    cv2.imshow("image", image)
    cv2.imshow("normalized", normalized)
    cv2.imshow("equalized", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
