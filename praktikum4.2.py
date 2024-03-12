# Kuantisasi Citra Gray Level 1, 2, 3, dan 4
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gambar.jpg',0)

img_gray = 128*np.floor(img/128)
gray1 = img_gray
img_gray = 64*np.floor(img/64)
gray2 = np.uint8(img_gray)
img_gray = 32*np.floor(img/32)
gray3 = np.uint8(img_gray)
img_gray = 16*np.floor(img/16)
gray4 = np.uint8(img_gray)

titles = [u'(a) Kuantisasi Gray L1', u'(b) Kuantisasi Gray L2', u'(c) Kuantisasi Gray L3',
          u'(d) Kuantisasi Gray L4']

images = [gray1, gray2, gray3, gray4]

for i in range(4):
    plt.subplot(2, 2, i+1),
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()