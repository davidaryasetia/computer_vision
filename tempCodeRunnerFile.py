import cv2

img = cv2.imread("gambar.jpg")

print("Ukuran Image", img.shape)
print("Type data", img.dtype)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()