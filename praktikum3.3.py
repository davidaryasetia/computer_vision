# Percobaan 3 : Grayscale dengan Iluminasi Citra

import cv2 
import numpy as np 
img = cv2.imread("gambar.jpg")

# Memisahkan sauran warna : menjadi (R),(G),(B) dengan fungsi split
B,G,R = cv2.split(img)

''' Menghitung rata-rata intensitas warna
    dari saluran R, G, B
'''
img_gray1 = 0.33 * R + 0.33 * G + 0.33 * B
img_gray1 = img_gray1.astype(np.uint8)
img_RG1 = np.minimum(R,G)

img_gray2 = np.minimum(img_RG1,B)
img_RG2 = np.maximum(R,G)
img_gray3 = np.maximum(img_RG2,B)

cv2.imshow("Iluminasi Rata Rata",img_gray1)
cv2.imshow("Ilumninasi minimum",img_gray2)
cv2.imshow("Ilumninasi maksimum",img_gray3)
cv2.waitKey(0)
cv2.destroyAllWindows()