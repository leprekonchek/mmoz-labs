import numpy as np


def morphological(image):
    mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    binary_img = np.zeros(image.shape, dtype=np.uint8)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y] == 255:
                binary_img[x, y] = 1

    res_bin_image = np.zeros(image.shape, dtype=np.uint8)

    for x in range(image.shape[0] - 1):
        for y in range(image.shape[1] - 1):
            right = 0
            for i in range(3):
                for j in range(3):
                    if binary_img[x + i - 1, y + j - 1] and mask[i, j]:
                        right += 1
            if right == 9:
                res_bin_image[x, y] = binary_img[x, y] or 1

    res_bin_image = difference(binary_img, res_bin_image)

    res_image = np.zeros(image.shape, dtype=np.uint8)
    for x in range(res_bin_image.shape[0]):
        for y in range(res_bin_image.shape[1]):
            if res_bin_image[x, y] == 1:
                res_image[x, y] = 255
    return res_image


def difference(minuend, subtrahend):
    difference_array = np.zeros(minuend.shape, dtype=np.uint8)
    for x in range(minuend.shape[0] - 1):
        for y in range(minuend.shape[1] - 1):
            if minuend[x, y] and not subtrahend[x, y]:
                    difference_array[x, y] = minuend[x, y]
    return difference_array
