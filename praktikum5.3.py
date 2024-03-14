# Percobaan 3 : Invers
import cv2
import numpy as np 
import matplotlib.pyplot as plt

# Membaca dan mengubah citra menjadi 0
img = cv2.imread("gambar.jpg", 0)

 # Melakukan invers pada nilai piksel dengen mengurangkan setiap nilai piksel dari 255
img1 = 255 - img
plt.subplot(121)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Original")
plt.subplot(122)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("invers")
plt.show()