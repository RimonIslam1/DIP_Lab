import cv2
import numpy as np

img = cv2.imread("iphone.jpg")

img = cv2.resize(img, (400, 600))

bright_image = np.clip(img.astype(np.float32) + 100, 0, 255).astype(np.uint8)

def threshold_pixel(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if img[i, j, k] < 128:
                    img[i, j, k] = 0
                else:
                    img[i, j, k] = 255

threshold_image = img.copy()
threshold_pixel(threshold_image)

combined = np.hstack((img, bright_image, threshold_image))

cv2.imshow("Original vs Brightened vs Threshold", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()