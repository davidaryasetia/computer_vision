# Percobaan 4 : Transformasi Exponensial 
import cv2
import numpy as np 

img = cv2.imread("gambar.jpg", 0)

# Mengkonversi nilai piksel dalam gambar ke dalam skala 0 hingga1 dengan membagi tiap piksel dengan 255
img = img/255
img1 = 100.*np.exp(0.5*img)
img1 = np.uint8(img1)

img2 = 50.*np.exp(0.5*img)
img2 = np.uint8(img2)

cv2.imshow("Original Image", img)
cv2.imshow("a=100 b=0.5", img1)
cv2.imshow("a=50, b=2.0", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()