import cv2

img = cv2.imread("gambar.jpg")

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

cv2.imshow('Original Image',img)
cv2.imshow('B-RctrGB',b)
cv2.imshow('G-RGB',g)
cv2.imshow('R-RGB',r)

cv2.waitKey()
cv2.destroyAllWindows()