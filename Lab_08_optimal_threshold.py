import numpy as np


def optimal_threshold(image):
    hist = cdf(image)
    res_image = np.copy(image)
    tk = 0
    tk1 = 128
    while tk1 != tk:
        u = sum([i * hist[i] for i in range(tk1)]) / sum([hist[i] for i in range(tk1)])
        uu = sum([i * hist[i] for i in range(tk1 + 1, 256)]) / sum([hist[i] for i in range(tk1 + 1, 256)])
        tk = tk1
        print(tk1)
        tk1 = int((u + uu) / 2)

    res_image[res_image <= tk1] = 0
    res_image[res_image > tk1] = 255

    return res_image


def cdf(image):
    cdf = [0] * 256
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            cdf[image[i][j]] += 1
    return cdf
