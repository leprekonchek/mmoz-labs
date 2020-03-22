import math
import numpy as np


def gauss(image, sigma, size_n):
    mes = int(size_n / 2)
    img_res = np.copy(image)

    mask = []
    gauss_mask = 0
    for i in range(-mes, mes + 1):  # маска
        mask_row = []
        for j in range(-mes, mes + 1):
            mask_row.append(gauss_function(i, j, sigma))
            gauss_mask += mask_row[-1]
        mask.append(mask_row)

    for x in range(image.shape[0] - mes):  # row
        for y in range(image.shape[1] - mes):  # columns
            sum_ = 0
            for i in range(-mes, mes + 1):
                for j in range(-mes, mes + 1):
                    sum_ += image.item(x + i, y + j) * mask[i + mes][j + mes]
            img_res[x][y] = sum_ / gauss_mask
    return img_res


def gauss_function(im_x, im_y, sigma):
    power = -((im_x ** 2 + im_y ** 2) / (2 * (sigma ** 2)))
    return (1 / (2 * math.pi * (sigma ** 2))) * (math.e ** power)


def kernel(image, matrix):
    length = len(matrix)
    img_res = np.copy(image)

    for x in range(image.shape[0] - length):  # row
        for y in range(image.shape[1] - length):  # columns
            sum_ = 0
            for i in range(length):
                for j in range(length):
                    sum_ += image[x + i][y + j] * matrix[i][j]
            img_res[x][y] = sum_ / 16
    return img_res
