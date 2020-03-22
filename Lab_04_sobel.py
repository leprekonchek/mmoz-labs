import numpy as np
import Lab_05_cannie as cn
import math


def sobel(image):
    g1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    g2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    angles = np.zeros(image.shape, dtype=np.uint8)
    img_res = np.copy(image)
    for x in range(image.shape[0] - 1):
        for y in range(image.shape[1] - 1):
            sum1 = 0
            sum2 = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sum1 += image.item(x + i, y + j) * g1.item(i + 1, j + 1)
                    sum2 += image.item(x + i, y + j) * g2.item(i + 1, j + 1)
            img_res[x][y] = math.sqrt(sum1 ** 2 + sum2 ** 2) / 4
            angle = np.arctan2(sum1, sum2) * 180 / math.pi
            angles[x][y] = cn.normalize_angle(angle)
    return img_res, angles


def sobelY(image):
    g1 = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    img_res = np.copy(image)
    for x in range(image.shape[0] - 1):
        for y in range(image.shape[1] - 1):
            sum1 = 0
            sum2 = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sum1 += image[x + i][y + j] * g1[i + 1][j + 1]
            img_res[x][y] = math.sqrt(sum1 ** 2 + sum2 ** 2) / 4
    return img_res


def sobelX(image):
    g2 = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

    img_res = np.copy(image)
    for x in range(image.shape[0] - 1):
        for y in range(image.shape[1] - 1):
            sum1 = 0
            sum2 = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sum2 += image[x + i][y + j] * g2[i + 1][j + 1]
            img_res[x][y] = math.sqrt(sum1 ** 2 + sum2 ** 2) / 4
    return img_res
