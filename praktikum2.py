#TEsting

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img=cv2.imread("gambar.jpg")

print("ukuran image",img.shape)
height,width=img.shape[0],img.shape[1]

print("Tipe data",img.dtype)
cv2.imshow("Original Image",img)

new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height,width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)

#Tugas Praktikum 
new_img4 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
new_img5 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

print(img[136,413])
new_img1=img.copy()
new_img1[136:146,413:423] = (0,255,0)
cv2.imshow("Update Image setPixel",new_img1)

for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img2[i,j][k] = img[i,j][k]
cv2.imshow("Image copy",new_img2)

for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img3[i,j][k] = img[height-1-i,j][k]
cv2.imshow("Image Flip",new_img3)

cv2.imshow("Rotate 90 Clockwise",new_img4)
cv2.imshow("Routate 90 CounterClockWise",new_img5)

img_flip_horizontal = cv2.flip(img, flipCode=1)
ing_flip_vertical = cv2.flip(img, flipCode=0)
img_flip_both=cv2.flip(img,-1)

plt.figure(figsize=(10,10))
plt.suplot(221).plt.imshow(cv2.cvtColor(img))


cv2.waitKey(0)
cv2.destroyAllWindows()