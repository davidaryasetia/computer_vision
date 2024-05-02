# Percobaan 2 : Contrast 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("gambar.jpg", 0)

img1 = img * 0.5
img2 = img * 0.75
img3 = img * 1.25
img4 = img * 1.5

plt.subplot(141)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.subplot(142)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.subplot(143)
plt.imshow(img3, cmap='gray', vmin=0, vmax=255)
plt.subplot(144)
plt.imshow(img4, cmap='gray', vmin=0, vmax=255)
plt.show()