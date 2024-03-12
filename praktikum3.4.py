# Percobaan 4 : Citra binary
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
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(img, 127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','Binary','BINARY_INV','TRUNC','TOZERO','TOSERA_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6): 
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()