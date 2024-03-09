#Percobaan 1 : Layer B/G/R

import cv2

img = cv2.imread("gambar.jpg")


# Set ke blue index 1(G)=0 2(R)=0
b=img.copy()
b[:,:,1]=0
b[:,:,2]=0

g=img.copy()
g[:,:,0]=0
g[:,:,2]=0
cv2.imshow('G-RGB',g)

r=img.copy()
r[:,:,0]=0
r[:,:,1]=0

cv2.imshow('original image',img)
cv2.imshow('B-RGB',b)
cv2.imshow('G-RGB',g)
cv2.imshow('R-RGB',r)

cv2.waitKey(0)
cv2.destroyAllWindows()
