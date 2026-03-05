import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('image.jpg').convert('L')
f = np.array(img, dtype=float)

M, N = f.shape

m = 3
n = 3
pad_x = m // 2
pad_y = n // 2

padded = np.zeros((M + 2*pad_x, N + 2*pad_y))

for i in range(M):
    for j in range(N):
        padded[i + pad_x][j + pad_y] = f[i][j]

g = np.zeros((M, N))

for x in range(M):
    for y in range(N):

        total = 0

        for s in range(m):
            for t in range(n):
                total += padded[x + s][y + t]

        g[x][y] = total / (m * n)  

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(f, cmap='gray')

plt.subplot(1,2,2)
plt.title("Blurred (Averaging)")
plt.imshow(g, cmap='gray')

plt.show()