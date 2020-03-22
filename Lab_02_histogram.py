def calc_cdf(image):
    freq = [0] * 256
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            freq[image[i][j]] += 1
    return freq


def equalize(image, cdf):
    cdf_normal = [0] * 256
    cdf_min = max(cdf)
    n = image.shape[0] * image.shape[1]
    cur_sum = 0
    for i in range(256):
        if cdf[i] != 0:
            cur_sum += cdf[i]
            if cur_sum < cdf_min:
                cdf_min = cur_sum
            cdf_normal[i] = round((cur_sum - cdf_min) / (n - cdf_min) * 255)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = cdf_normal[image[i][j]]
    return image
