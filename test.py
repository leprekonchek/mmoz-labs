import cv2 as cv


def find_dir(direction, image, x, y):
    cases = \
        {
            0: (x + 1, y),
            1: (x + 1, y + 1),
            2: (x, y + 1),
            3: (x - 1, y + 1),
            4: (x - 1, y),
            5: (x - 1, y - 1),
            6: (x, y - 1),
            7: (x + 1, y - 1)
        }
    print("x y ", x, y)
    for i in range(8):
        if direction > 7:
            direction = 0
        (x1, y1) = cases[direction]
        print("x1 y1 ", x1, y1)
        if image[x1, y1] == 255:
            return direction
        else:
            direction += 1
    return direction, x1, y1


img = cv.imread("./pics/contour.tif", cv.IMREAD_GRAYSCALE)
dir, xx, yy = find_dir(5, img, 100, 210)
print(dir, xx, yy)

