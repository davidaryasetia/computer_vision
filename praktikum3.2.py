# Percobaan 2 : Grayscale dari B/G/R

import cv2

img = cv2.imread("gambar.jpg")

# Memisahkan gambar ke 3 saluran warna B G R 
B, G, R = cv2.split(img)

cv2.imshow("Original image",img)
cv2.imshow("Channel R",R)
cv2.imshow("Channel G",G)
cv2.imshow("Channel B",B)

cv2.waitKey(0)
cv2.destroyAllWindows()