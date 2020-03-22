import numpy as np
import scipy


def harris(image):
    k = 0.04
    Threshold = 50000
    sigma = 1
    halfwid = sigma * 3

    matrix = [xx, yy] = np.meshgrid(-halfwid, halfwid)

    for i in range(len(matrix)):
        Gxy = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))

    for i in range(len(matrix)):
        Gx = xx * np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))
        Gy = yy * np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))

    I = image

    # 1) Compute x and y derivatives of image
    Ix = scipy.signal.convolve2d(Gx, I)
    Iy = scipy.signal.convolve2d(Gy, I)

    # 2) Compute products of derivatives at every pixel
    Ix2 = [Ix[i] ** 2 for i in range(len(Ix))]
    Iy2 = [Iy[i] ** 2 for i in range(len(Iy))]
    Ixy = [Ix[i] * Iy[i] for i in range(len(Ix + Iy))]

    # 3)Compute the sums of the products of derivatives at each pixel
    Sx2 = scipy.signal.convolve2d(Gxy, Ix2)
    Sy2 = scipy.signal.convolve2d(Gxy, Iy2)
    Sxy = scipy.signal.convolve2d(Gxy, Ixy)

    im = np.zeros(image.shape[0], image.shape[1])
    for x in range(1, image.shape[0]):
        for y in range(1, image.shape[1]):
            # 4) Define at each pixel(x, y) the matrix H
            H = [Sx2(x, y), Sxy(x, y),
                 Sxy(x, y), Sy2(x, y)]

            # 5) Compute the response of the detector at each pixel
            R = np.det(H) - k * (np.trace(H) ** 2)

            #  6) Threshold on value of R
            if R > Threshold:
                image[x, y] = R

    # 7) Compute nonmax suppression
    output = im > scipy.ndimage.morphology.binary_dilation(im, [[1, 1, 1],
                                                                      [1, 0, 1],
                                                                      [1, 1, 1]])
    return output
