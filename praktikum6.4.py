# Percobaan 4 : Auto Level Gray Scale
import cv2
import numpy as np 

img = cv2.imread("gambar.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x_min = np.min(img_gray)
x_max = np.max(img_gray)
print(x_min)
print(x_max)
sk = 255./ (x_max-x_min)
img1 = sk * (img_gray-x_min)
img1 = np.uint8(img1)
cv2.imshow("Original", img_gray)
cv2.imshow("Enchaced", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()