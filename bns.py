import cv2
import numpy as np


def findCorners(image, w_size, k, threshold):
    res_img = np.copy(image)
    color_img = cv2.cvtColor(res_img, cv2.COLOR_GRAY2RGB)

    offset = w_size // 2

    dy, dx = np.gradient(image)
    Ix2 = dx ** 2
    Iy2 = dy ** 2
    Ixy = dy * dx

    # Loop through image and find our corners
    for y in range(offset, image.shape[0] - offset):
        for x in range(offset, image.shape[1] - offset):
            # Calculate sum of squares
            w_Ix2 = Ix2[y - offset:y + offset + 1, x - offset:x + offset + 1]
            w_Iy2 = Iy2[y - offset:y + offset + 1, x - offset:x + offset + 1]
            w_Ixy = Ixy[y - offset:y + offset + 1, x - offset:x + offset + 1]
            sum_x2 = w_Ix2.sum()
            sum_y2 = w_Iy2.sum()
            sum_xy = w_Ixy.sum()

            # Find determinant and trace, use to get corner response
            det = (sum_x2 * sum_y2) - (sum_xy ** 2)
            trace = sum_x2 + sum_y2
            r = det - k * (trace ** 2)

            # If corner response is over threshold, color the point and add to corner list
            if r > threshold:
                print(x, y, r)
                color_img.itemset((y, x, 0), 0)
                color_img.itemset((y, x, 1), 0)
                color_img.itemset((y, x, 2), 255)
    return color_img


def main():
    img = cv2.imread("./pics/man.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("original image", img)
    cv2.waitKey()

    cv2.imshow("final image", findCorners(img, 3, 0.04, 50000))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
