import numpy as np


def curvature(list, k):
    # creating list for our curvature values
    curv_list = []
    for i in range(len(list) - k):
        # current pixel
        pix = list[i][0]  # x
        piy = list[i][1]  # y from list (x, y)
        # forward vector
        pfx = list[i + k][0]
        pfy = list[i + k][1]
        # backward vector
        pbx = list[i - k][0]
        pby = list[i - k][1]

        ob = angles(pix, piy, pbx, pby)  # angles of backward vector
        of = angles(pix, piy, pfx, pfy)  # angles of forward vector
        distb = distance(pix, piy, pbx, pby)  # distance (size) of the backward vector
        distf = distance(pix, piy, pfx, pfy)  # distance (size) of the forward vector

        ki = (angles_difference(ob, of) * (distb + distf)) / (2 * distb * distf)  # final value of the curvature
        curv_list.append(ki)
    return curv_list


def distance(x1, y1, x2, y2):
    return abs(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


def angles(x1, y1, x2, y2):
    if (y2 - y1) == 0:
        return 0
    else:
        return np.arctan((x2 - x1) / (y2 - y1))


def angles_difference(ob, of):
    oi = ob / 2 + of / 2
    delf = of - oi  #дельта ф
    return delf
