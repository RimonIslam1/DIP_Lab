import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('image.jpg').convert('L')
f = np.array(img, dtype=float)

M, N = f.shape

padded = np.zeros((M+2, N+2))

for i in range(M):
    for j in range(N):
        padded[i+1][j+1] = f[i][j]

g = np.zeros((M, N))

for x in range(1, M+1):
    for y in range(1, N+1):

        laplacian = (
            padded[x+1][y] + padded[x-1][y] +
            padded[x][y+1] + padded[x][y-1] -
            4 * padded[x][y]
        )

        g[x-1][y-1] = padded[x][y] - laplacian

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(f, cmap='gray')

plt.subplot(1,2,2)
plt.title("Sharpened")
plt.imshow(g, cmap='gray')

plt.show()