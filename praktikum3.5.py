# Tugas praktikum 1 : proses sephia
import numpy as np 
import cv2 
img = cv2.imread("gambar.jpg")

B,G,R = cv2.split(img)

# declare variable BGR baru dan modifikasi saluran 
R_new = 2 * R
G_new = 1.8 * R
B_new = R

# Memastikan tipe data sama untuk semua saluran 
R_new = R_new.astype(np.uint8)
G_new = G_new.astype(np.uint8)
B_new = B_new.astype(np.uint8)

# Menggabungkan saluran warna yang telah dimodifikasi
sephia = cv2.merge([B_new, G_new, R_new])
cv2.imshow("Original Image : ", img)
cv2.imshow("Hasil Merge Sephia Project", sephia)
cv2.imshow("Layer B_new", B_new)
cv2.imshow("Layer G_new", G_new)
cv2.imshow("Layer R_new", R_new)

cv2.waitKey(0)
cv2.destroyAllWindows()