# Percobaan 3 => Citra + Noise
import numpy as np 
import cv2

img = cv2.imread("gambar.jpg")
noise = np.random.rand(*img.shape) * 10
img_noise = np.abs(img + noise)
img_noise = np.uint8(img_noise)

cv2.imshow("Original", img)
cv2.imshow("Imaage Noise", img_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()