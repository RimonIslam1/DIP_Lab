import cv2
import numpy as np
import matplotlib.pyplot as plt


def gamma_transformation_loop(image, gamma):
    height, width, channels = image.shape

    output = np.zeros((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels): 

                r = image[i, j, k] / 255.0

                s = r ** gamma

                output[i, j, k] = int(s * 255)

    return output


image_path = "image.jpg"
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gamma_value = 0.5   

output_image_1 = gamma_transformation_loop(image_rgb, gamma_value)

gamma_value = 0.3   

output_image_2 = gamma_transformation_loop(image_rgb, gamma_value)


output_image_3 = gamma_transformation_loop(image_rgb, gamma_value)
plt.figure(figsize=(10, 5))

plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title("Input Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(output_image_1)
plt.title(f"Gamma = 0.5")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(output_image_2)
plt.title(f"Gamma = 0.3")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(output_image_3)
plt.title(f"Gamma = 1.6")
plt.axis("off")
plt.show()
plt.tight_layout()