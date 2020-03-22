import numpy as np


def region_growth(image, threshold):
    bool_array = np.zeros(image.shape, np.uint8)
    res_image = np.zeros(image.shape, np.uint8)

    label = 40
    labels = []
    for x in range(image.shape[0] - 1):
        for y in range(image.shape[1] - 1):
            if bool_array[x, y] == 1:
                continue
            if label == 250:
                label = 0  # label % 255
            stack = [(x, y)]
            while stack:
                (x1, y1) = stack.pop()
                for i in range(3):
                    for j in range(3):
                        temp1 = x1 + i - 1
                        temp2 = y1 + j - 1
                        if temp1 < 0 or temp1 >= image.shape[0] or temp2 < 0 or temp2 >= image.shape[1]:
                            continue
                        if bool_array[temp1, temp2] == 1:
                            continue

                        if abs(image.item(x1, y1) - image.item(temp1, temp2)) <= threshold:
                            # if label == 160:
                            res_image[temp1, temp2] = label
                            bool_array[temp1, temp2] = 1
                            stack.append((temp1, temp2))
        labels.append(label)
        label += 10
    print(labels)
    return res_image
