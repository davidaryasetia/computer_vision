# Percobaan 4.1 melakukan kuantitatsi pada gambar

import cv2 
import numpy as np 

img = cv2.imread("gambar.jpg")
height, width = img.shape[0], img.shape[1]

new_img = np.zeros((height, width, 3), np.uint8)

# Quantification level 2
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 128:
                gray=0
            else: 
                gray=129
            new_img[i, j][k] = np.uint8(gray)

# Show image 
cv2.imshow('original image', img)
cv2.imshow('new',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()