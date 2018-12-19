import cv2
import numpy as np


def lab_11_transform(filename):
    # Geometric alignment
    image = cv2.imread(filename)
    height, width, channels = image.shape

    # Perspective transformation
    src = np.array([
        [22, 105],
        [160, 21],
        [234, 138],
        [98, 224],
    ], dtype="float32")

    dst = np.array([
        [0, 0],
        [width, 0],
        [width, height],
        [0, height],
    ], dtype="float32")

    transform = cv2.getPerspectiveTransform(src, dst)
    warp = cv2.warpPerspective(image, transform, (width, height))

    cv2.imshow("image", image)
    cv2.imshow("warpPerspective", warp)

    # Bilinear transformation
    map_x = np.array([[0] * width] * height, dtype="float32")
    map_y = np.array([[0] * width] * height, dtype="float32")

    for i in range(height):
        for j in range(width):
            map_x[i, j] = 1.2 * j - 0.9 * i + 90
            map_y[i, j] = 1.5 * i + 0.9 * j - 180

    remap = cv2.remap(warp, map_x, map_y, cv2.INTER_LINEAR)

    cv2.imshow("remap", remap)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
