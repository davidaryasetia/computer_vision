import cv2 
import numpy as np 

img=cv2.imread('gambar.jpg')
print("ukuran image", img.shape)
height, width = img.shape[0], img.shape[1]
print("Type data",img.dtype)

cv2.imshow("Image", img)

new_img1=np.zeros((height, width, 3). np.unint8)
new_img2=np.zeros((height, width, 3). np.unint8)
new_img3=np.zeros((height, width, 3). np.unint8)

print(img(136,413))
new_img1=img.copy()
new_img1[136:146,413:423] = (0, 255, 0)

cv2.imshow("image Set Pixel", new_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
