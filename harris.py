import cv2 as cv
import numpy as np


def harris(image, threshold, window):
    height = image.shape[0]
    width = image.shape[1]
    window_size = 3

    corners = np.zeros((height, width))
    # sobel
    Ix = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
    Iy = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)

    Ix2 = Ix ** 2
    Iy2 = Iy ** 2

    offset = window_size // 2
    for x in range(offset, height - offset):
        for y in range(offset, width - offset):
            sxx = np.sum(Ix2[x - offset:x + 1 + offset, y - offset:y + 1 + offset])
            syy = np.sum(Iy2[x - offset:x + 1 + offset, y - offset:y + 1 + offset])


            r = min(sxx, syy)

            if r > threshold:
                corners[x][y] = r
                # print(r)

    # non max supression
    out_features = []
    d_x = window
    d_y = window

    x = 0
    while x < height - d_x:
        y = 0
        while y < width - d_y:
            window = corners[x:x + d_x, y:y + d_y]
            if window.size == 0:
                continue

            local_max = window.max()
            max_coord = np.unravel_index(np.argmax(window, axis=None), window.shape)

            # suppress everything
            corners[x:x + d_x, y:y + d_y] = 0

            # reset only the max
            if local_max > 0:
                # print(local_max)
                max_x = max_coord[0] + x
                max_y = max_coord[1] + y
                corners[max_x, max_y] = local_max
                out_features.append((max_x, max_y))
                # print("max coordinate is ", (max_x, max_y))

            y += d_y
        x += d_x

    return out_features


def draw_img(color_img, features):
    out = color_img.copy()
    for corners in features:
        y, x = corners
        cv.circle(out, (x, y), 1, [0, 0, 255], -1)
    return out


def draw_circles(shape, features):
    out = np.zeros(shape, np.uint8)
    for corners in features:
        y, x = corners
        # Circling the corners in green
        cv.circle(out, (x, y), 3, 255, -1)
    return out


if __name__ == '__main__':
    img = "pics/geneva.tif"

    bw_image = cv.imread(img, cv.IMREAD_GRAYSCALE)
    color_img = cv.imread(img, cv.IMREAD_COLOR)

    cv.imshow("original image", color_img)
    cv.waitKey(0)
    cv.imshow("corner detection", draw_img(color_img, harris(bw_image, 10000, 10)))

    cv.waitKey(0)
    cv.destroyAllWindows()
