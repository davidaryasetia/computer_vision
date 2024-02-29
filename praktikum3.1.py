import cv2

img=cv2.imread("gambar.jpg")

B,G,R = cv2.split(img)
cv2.imshow("Original Image",img)
cv2.imshow("Channel R",R)
cv2.imshow("Channel G",G)
cv2.imshow("Channel B",B)
cv2.waitKey(0)
cv2.destroyAllW