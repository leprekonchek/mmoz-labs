import Lab_03_gaussian as gaus
import Lab_04_sobel as sb
import numpy as np
import cv2 as cv


def canny_detect(image, low, high):
    blur_img = gaus.gauss(image, 1.4, 5)  # blurred image
    sobel, angles = sb.sobel(blur_img)  # sobel b&w and gradient angle of each pixel
    image4 = non_max_suppress(sobel, angles)  # angles, image
    image5 = threshold_hysteresis(image4, low, high)  # which borders we include in
    return {'img0': blur_img, 'img1': sobel, 'img2': angles, 'img3': image4, 'img4': image5}


def normalize_angle(angle_val):
    if angle_val < 0:
        angle_val += 360
    while angle_val > 180:
        angle_val -= 180
    if 22.5 >= angle_val >= 0 or 180 >= angle_val > 157.5:
        angle_val = 0
    elif 67.5 >= angle_val > 22.5:
        angle_val = 45
    elif 112.5 >= angle_val > 67.5:
        angle_val = 90
    elif 157.5 >= angle_val > 112.5:
        angle_val = 135
    return angle_val


def non_max_suppress(image, angles):
    maxes = np.zeros(angles.shape, dtype=np.uint8)
    for x in range(image.shape[0] - 1):
        for y in range(image.shape[1] - 1):
            if angles.item(x, y) == 0:
                if max(image[x, y], image[x, y + 1], image[x, y - 1]) == image[x, y]:
                    maxes[x, y] = image.item(x, y)
            elif angles.item(x, y) == 45:
                if max(image[x, y], image[x + 1, y + 1], image[x - 1, y - 1]) == image[x, y]:
                    maxes[x, y] = image.item(x, y)
            elif angles.item(x, y) == 90:
                if max(image[x, y], image[x + 1, y], image[x - 1, y]) == image[x, y]:
                    maxes[x, y] = image.item(x, y)
            elif angles.item(x, y) == 135:
                if max(image[x, y], image[x - 1, y + 1], image[x + 1, y - 1]) == image[x, y]:
                    maxes[x, y] = image.item(x, y)
    print(np.max(maxes))
    return maxes


def threshold_hysteresis(image, low, high):
    final_image = np.zeros(image.shape, dtype=np.uint8)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x][y] >= high:
                final_image[x, y] = 255
            if high > image[x][y] >= low:
                if image[x + 1, y] == 255 or image[x - 1, y] == 255 or image[x, y - 1] == 255 or \
                        image[x, y + 1] == 255 or image[x + 1, y + 1] == 255 or \
                        image[x - 1, y - 1] == 255 or image[x + 1, y - 1] == 255 or \
                        image[x - 1, y + 1] == 255:
                    final_image[x, y] = 255
    return final_image
