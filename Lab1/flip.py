import cv2
import numpy as np

img = cv2.imread("iphone.jpg")
img = cv2.resize(img, (300, 300))
 
vertical_flip = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        vertical_flip[i, j] = img[img.shape[0] - 1 - i, j]

combined = np.hstack((img, vertical_flip))

cv2.imshow("Original | Vertical Flip", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()