import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(img):

    hist = [0] * 256

    for row in img:
        for pixel in row:
            hist[pixel] += 1

    total = img.shape[0] * img.shape[1]

    pdf = [h / total for h in hist]
    
    cdf = [0] * 256
    cdf[0] = pdf[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf[i]

    mapping = [round(255 * c) for c in cdf]

    new_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i, j] = mapping[img[i, j]]

    return new_img


def show_three_images(img1, img2, img3, titles=None, cmap='gray'):
    imgs = [img1, img2, img3]
    if titles is None:
        titles = ['', '', '']
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, im, t in zip(axes, imgs, titles):
        if im is None:
            ax.axis('off')
            ax.set_title(t)
            continue
        if len(im.shape) == 2:
            ax.imshow(im, cmap=cmap)
        else:
            ax.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
        ax.set_title(t)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    # load image (grayscale)
    img = cv2.imread("image.jpg", 0)
    if img is None:
        print("image.jpg not found. Place an image named 'image.jpg' in the script folder.")
        return

    # compute custom equalization and OpenCV equalization
    result = histogram_equalization(img)
    eq_cv = cv2.equalizeHist(img)

    # save result
    cv2.imwrite("equalized.jpg", result)
    print("Histogram Equalization completed. Showing results...")

    # display original and equalized images with their histograms
    def show_two_images_and_histograms(orig, equalized, titles=None):
        imgs = [orig, equalized]
        if titles is None:
            titles = ['Original', 'Equalized']
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        # Top row: images
        for i, imgx in enumerate(imgs):
            ax = axes[0, i]
            ax.imshow(imgx, cmap='gray')
            ax.set_title(titles[i])
            ax.axis('off')

        # Bottom row: histograms
        for i, imgx in enumerate(imgs):
            ax = axes[1, i]
            hist = cv2.calcHist([imgx], [0], None, [256], [0, 256])
            ax.plot(hist, color='black')
            ax.set_xlim([0, 255])
            ax.set_xlabel('Intensity')
            ax.set_ylabel('Count')
            ax.set_title(f"Histogram - {titles[i]}")

        plt.tight_layout()
        plt.show()

    show_two_images_and_histograms(img, result, titles=["Original", "Custom Equalized"]) 
if __name__ == "__main__":
    main()
