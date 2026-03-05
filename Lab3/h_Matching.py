import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_cdf(image):

    hist = [0] * 256

    for row in image:
        for pixel in row:
            hist[pixel] += 1

    total = image.shape[0] * image.shape[1]

    pdf = [h / total for h in hist]

    cdf = [0] * 256
    cdf[0] = pdf[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf[i]

    return cdf


def histogram_matching(source, target):

    cdf_source = calculate_cdf(source)
    cdf_target = calculate_cdf(target)

    mapping = [0] * 256

    for i in range(256):
        diff = abs(cdf_source[i] - cdf_target[0])
        index = 0

        for j in range(256):
            new_diff = abs(cdf_source[i] - cdf_target[j])
            if new_diff < diff:
                diff = new_diff
                index = j

        mapping[i] = index

    matched = np.zeros_like(source)

    for i in range(source.shape[0]):
        for j in range(source.shape[1]):
            matched[i, j] = mapping[source[i, j]]

    return matched


def show_images_and_histograms(source, target, matched, titles=None):
    imgs = [source, target, matched]
    if titles is None:
        titles = ['Source', 'Target', 'Matched']

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))

    # Top row: images
    for i, img in enumerate(imgs):
        ax = axes[0, i]
        if img is None:
            ax.axis('off')
            continue
        ax.imshow(img, cmap='gray')
        ax.set_title(titles[i])
        ax.axis('off')

    # Bottom row: histograms
    for i, img in enumerate(imgs):
        ax = axes[1, i]
        if img is None:
            ax.axis('off')
            continue
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        ax.plot(hist, color='black')
        ax.set_xlim([0, 255])
        ax.set_xlabel('Intensity')
        ax.set_ylabel('Count')
        ax.set_title(f"Histogram - {titles[i]}")

    plt.tight_layout()
    plt.show()


def main():
    source = cv2.imread("image.jpg", 0)
    target = cv2.imread("target.jpg", 0)

    if source is None or target is None:
        print("Missing 'image.jpg' or 'target.jpg' in the script folder.")
        return

    result = histogram_matching(source, target)
    cv2.imwrite("matched.jpg", result)
    print("Histogram Matching completed. Showing results...")
    show_images_and_histograms(source, target, result, titles=["Source", "Target", "Matched"])


if __name__ == "__main__":
    main()
