# Percobaan 3 : Histogram Level 
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("gambar.jpg")
img = np.uint8(img)
img1 = 255 - img
img1 = np.uint8(img1)

hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img1], [0], None, [256], [0, 256])

plt.subplot(211)
plt.axis('off')
plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(222)
plt.plot(hist1)
plt.grid()
plt.xlim([0, 255])

plt.subplot(222)
plt.axis('off')
plt.title("Invers")
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.subplot(224)
plt.plot(hist2)
plt.grid()
plt.xlim([0, 255])
plt.show()