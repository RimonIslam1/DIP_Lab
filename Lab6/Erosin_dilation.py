import numpy as np

def pad_image(image, k_h, k_w):
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    padded = np.zeros((image.shape[0] + 2*pad_h,
                       image.shape[1] + 2*pad_w), dtype=int)
    
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

image = np.array([
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
])

kernel = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

print("Original:\n", image)

print("\nErosion:\n", erosion(image, kernel))
print("\nDilation:\n", dilation(image, kernel))
print("\nOpening:\n", opening(image, kernel))
print("\nClosing:\n", closing(image, kernel))