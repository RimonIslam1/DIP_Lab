import cv2
from math import log, log2
import numpy as np


def rgb_to_gray(image_path):
    color_img = cv2.imread(image_path, 1)

    height, width, channels = color_img.shape

    gray_img = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            b, g, r = color_img[i, j]
            # Standard luminosity method to convert to grayscale
            gray_value = int(0.114 * b + 0.587 * g + 0.299 * r)
            gray_img[i, j] = gray_value

    return gray_img


img = rgb_to_gray("image.png")
# cv2.imshow("gray",img)
neg = img.copy()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        neg[i][j] = 255 - img[i][j]


def logg(img):
    logimg = img.copy()
    x_min = 200000
    x_max = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            v = log(img[i][j] + 1.0)
            if v < x_min:
                x_min = v
            if v > x_max:
                x_max = v
    diff = x_max - x_min
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            logimg[i][j] = int(255 * (log(img[i][j] + 1.0) - x_min) / diff)

    return logimg


def logg2(img):
    logimg = img.copy()
    x_max = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            v = log2(img[i][j] + 1.0)
            if v > x_max:
                x_max = v

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            logimg[i][j] = int(255 * (log2(img[i][j] + 1.0)) / x_max)

    return logimg


logimg = logg(img)
cv2.imshow("log", logimg)


logimg2 = logg2(img)
cv2.imshow("log2", logimg2)
cv2.waitKey(0)