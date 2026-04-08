import numpy as np
import matplotlib.pyplot as plt


def create_image(height=15, width=30):
    image = np.ones((height, width), dtype=np.uint8) * 255

    num_rects = 4
    rect_h = height // 3
    rect_w = width // 10
    gap = rect_w // 2

    top = (height - rect_h) // 2
    bottom = top + rect_h

    total_rects_width = num_rects * rect_w + (num_rects - 1) * gap
    left_start = (width - total_rects_width) // 2

    for i in range(num_rects):
        left = left_start + i * (rect_w + gap)
        right = left + rect_w
        image[top:bottom, left:right] = 0

    return image


def black_object_image_to_binary(image):
    return (image == 0).astype(int)



def plot_binary_images(images, titles):
    rows, cols = 2, 3
    plt.figure(figsize=(12, 7))

    for idx, (img, title) in enumerate(zip(images, titles), start=1):
        plt.subplot(rows, cols, idx)
        plt.imshow(img, cmap="gray", vmin=0, vmax=1)
        plt.title(title)
        plt.axis("off")

    for idx in range(len(images) + 1, rows * cols + 1):
        plt.subplot(rows, cols, idx)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


def pad_image(image, k_h, k_w):
    pad_h = k_h // 2
    pad_w = k_w // 2

    padded = np.zeros(
        (image.shape[0] + 2 * pad_h, image.shape[1] + 2 * pad_w), dtype=int
    )

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            padded[i + pad_h][j + pad_w] = image[i][j]

    return padded


def erosion(image, kernel):
    img_h, img_w = image.shape
    k_h, k_w = kernel.shape

    padded = pad_image(image, k_h, k_w)

    output = np.zeros((img_h, img_w), dtype=int)

    for i in range(img_h):
        for j in range(img_w):
            match = True

            for m in range(k_h):
                for n in range(k_w):
                    if kernel[m][n] == 1:
                        if padded[i + m][j + n] != 1:
                            match = False

            if match:
                output[i][j] = 1

    return output


def dilation(image, kernel):
    img_h, img_w = image.shape
    k_h, k_w = kernel.shape

    padded = pad_image(image, k_h, k_w)

    output = np.zeros((img_h, img_w), dtype=int)

    for i in range(img_h):
        for j in range(img_w):
            found = False

            for m in range(k_h):
                for n in range(k_w):
                    if kernel[m][n] == 1:
                        if padded[i + m][j + n] == 1:
                            found = True

            if found:
                output[i][j] = 1

    return output


def opening(image, kernel):
    eroded = erosion(image, kernel)
    opened = dilation(eroded, kernel)
    return opened


def closing(image, kernel):
    dilated = dilation(image, kernel)
    closed = erosion(dilated, kernel)
    return closed


raw_image = create_image(height=15, width=30)
image = black_object_image_to_binary(raw_image)

kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])



eroded_image = erosion(image, kernel)
dilated_image = dilation(image, kernel)
opened_image = opening(image, kernel)
closed_image = closing(image, kernel)



plot_binary_images(
    [image, eroded_image, dilated_image, opened_image, closed_image],
    ["Original (Binary)", "Erosion", "Dilation", "Opening", "Closing"],
)
