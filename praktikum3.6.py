# Tugas Praktikum 4 : Citra binary
import cv2
import numpy as np
from matplotlib import pyplot as plt 

# Membaca gambar dalam mode grayscale(0)
img = cv2.imread('gambar.jpg',0)

'''
Melakukan Thresholding : menggunakan beberapa metode thresholding
yang berbeda untuk menghasilkan citra biner dari gambar.
Thresholding -> mengubah citra ke dalam bentuk citra biner
'''
ret,global_thresholding = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
adaptive_mean_thresholding = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
adaptive_gaussian_thresholding = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original Image','Global Thresholding(v=127)','mean_thresholding','gaussian_thresholding']
images = [img, global_thresholding, adaptive_mean_thresholding, adaptive_gaussian_thresholding]

for i in range(4): 
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()