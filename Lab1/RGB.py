import cv2
import numpy as np

img = cv2.imread("iphone.jpg")
img = cv2.resize(img, (300, 300))

red_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
green_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
blue_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        blue_image[i, j, 0] = img[i, j, 0]
        green_image[i, j, 1] = img[i, j, 1]
        red_image[i, j, 2] = img[i, j, 2]

combined = np.hstack((red_image, green_image, blue_image))

cv2.imshow("Red Channel | Green Channel | Blue Channel", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()