import numpy as np


def average(my_list):
    return sum(my_list) / len(my_list)


def zoom_in(image, time):
    img_col = []

    for i in range(image.shape[0]):
        img_row = []
        for j in range(image.shape[1]):
            for t in range(time):
                img_row.append(image[i, j])
        for tt in range(time):
            img_col.append(img_row)
    return img_col


def zoom_out(image, time):
    img_col = []

    for i in range(0, image.shape[0] - time, time):
        img_row = []
        for j in range(0, image.shape[1] - time, time):
            arr = []
            arr.append(image[i][j])
            for k in range(time):
                arr.append(image[i + time][j])
                arr.append(image[i][j + time])
                arr.append(image[i + time][j + time])
            img_row.append(average(arr))
        img_col.append(img_row)
    return img_col


def black_white(image, number):
    # res_image = np.zeros(np.shape(image), np.uint8)
    # res_image[res_image <= number] = 0
    # res_image[res_image > number] = 255
    # return res_image
    img_col = []
    for i in range(image.shape[0]):
        img_row = []
        for j in range(image.shape[1]):
            if image[i][j] > number:
                img_row.append(0)
            else:
                img_row.append(255)
        img_col.append(img_row)
    return img_col
