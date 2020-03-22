import cv2 as cv
import numpy as np
import Lab_01_zoom as hm1
import Lab_02_histogram as hm2
import Lab_03_gaussian as hm3
import Lab_04_sobel as hm4
import Lab_05_cannie as hm5
import Lab_06_morpho_bin_edge as hm6
import Lab_07_regiongrowth as hm7
import Lab_08_optimal_threshold as hm8
import Lab_09_border_tracing as hm9
import Lab_10_contour_curvature as hm10
import Bonus_harris as bonus
from matplotlib import pyplot as plt


def main():
    img = cv.imread("./pics/chessboard.jpg", cv.IMREAD_GRAYSCALE)
    cv.imshow("original image", img)
    cv.waitKey()

    # # homework 1
    # # zoom in
    # cv.imshow("zoomed in", np.array(hm1.zoom_in(img, 3), np.uint8))
    # cv.waitKey(0)

    # # zoom out
    # cv.imshow("zoomed out", np.array(hm1.zoom_out(img, 3), np.uint8))
    # cv.waitKey(0)

    # # black and white
    # cv.imshow("black and white", np.array(hm1.black_white(img, 120), np.uint8))
    # cv.waitKey(0)

    # # homework 2
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    # cv.imshow("histogram equalization", np.array(hm2.equalize(img, hm2.calc_cdf(img)), np.uint8))
    # cv.waitKey(0)
    # plt.hist(hm2.equalize(img, hm2.calc_cdf(img)).ravel(), 256, [0, 256])
    # plt.show()

    # # homework 3
    # cv.imshow("gaussian blur", hm3.gauss(img, 1, 3))
    # cv.waitKey(0)
    #
    # matrix = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    # cv.imshow("kernel", hm3.kernel(img, matrix))
    # cv.waitKey(0)

    # # homework 4
    # cv.imshow("sobel X axis operator", hm4.sobelX(img))
    # cv.waitKey(0)
    #
    # cv.imshow("sobel Y axis operator", hm4.sobelY(img))
    # cv.waitKey(0)
    #
    # cv.imshow("sobel operator", hm4.sobel(img))
    # cv.waitKey(0)

    # # homework 5
    # images = hm5.canny_detect(img, 120, 10)
    # j = 0
    # for i in range(len(images)):
    #     j += 1
    #     cv.imshow(f"canny detector edges step {j}", images.get('img' + str(i)))
    #     cv.waitKey()

    # # homework 6 7 8
    # cv.imshow("morphological edge detection", hm6.morphological(img))
    # cv.waitKey()
    #
    # cv.imshow("region growth", hm7.region_growth(img, 50))
    # cv.waitKey()
    #
    # cv.imshow("optimal threshold", hm8.optimal_threshold(img))
    # cv.waitKey()

    # # homework 9
    # cv.imshow("border tracing", hm9.border_tracing(img))
    # cv.waitKey()
    #
    # # homework 10
    # plt.plot(hm10.curvature(hm9.border_list(img), 100))
    # plt.show()

    # # bonus
    cv.imshow("harris", bonus.harris(img))
    cv.waitKey()

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
