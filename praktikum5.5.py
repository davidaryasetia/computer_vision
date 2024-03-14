# Percobaan 5 : Logaritmik 
import cv2
import numpy as np 

img = cv2.imread("gambar.jpg", 0)

# Melakukan tranformasi logaritmuk pada gambar, parameter 40 dan 0.5
img1 = 40*np.log(0.5*img)
img1 = np.uint8(img1)

img2 = 40.*np.log(2.*img)
img2 = np.uint8(img2)
cv2.imshow("Original Image",img)
cv2.imshow("a=40 b=0.5", img1)
cv2.imshow("a=40 b=2.0", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
1) Perbedaan Brightness dan Contras 
Brightnes : 
- Kecerahan mengacu pada tingkat pencahayaan keseluruhan dari gambar
- Meningkatkan kecerahan akan membuat gambar secara keseluruhan terlihat lebih terang 
- manipulasi kecerahan dilakukan dengan menambah atau mengurangi nilai piksel dari setiap titik gambar

Contras : 
- Mengacu pada perbedaan antara nilai piksel yang berdekatan di dalam gambar
- Kontras tinggi berarti perbedaan antara are gelap dan terang dalam gambar sangat signifikan
- Manipulasi kontras dilakukan dengan memperluas atau mempersempit nilai pikse dalam gambar

2) Jika rumus brighnesss diganti dengan xb=xg+255 : 
   - makan nilai 255 akan ditambahkan ke setiap piksel dalam gambar 
   - akibatnya, setiap piksel dalam gambar akan dinaikkan nilainya sebesar 255, dan gambar akan menjadi sangat terang 
   - hasilnya gambar akan menjadi terlalu terang, bahkan bisa membuat piksel melebihi nilai maksimum 255, yang menyebabkan kehilangan detail

3) Jika rumus invers diganti dengan xb=128-xg : 
    - Rumus ini melakukan inversi pada nilai piksel dengan memindahkan titik tengah histogram (128 dalam skala grayscale) ke 0 dan mengurangi setiap nilai piksel dari 128. 
    - Akibatnya, piksel dengan nilai yang rendah akan menjadi lebih terang dan piksel dengan nilai yang tinggi akan menjadi lebih gelap.
    Dengan kata lain, area yang semula gelap akan menjadi terang dan sebaliknya, sehingga gambar akan memiliki efek negatif.
    Namun, perlu diperhatikan bahwa karena perhitungan dilakukan dalam skala integer, ada kemungkinan beberapa piksel menjadi negatif setelah transformasi, yang tidak mungkin dalam representasi gambar. Oleh karena itu, perlu dilakukan normalisasi atau penanganan khusus untuk menjaga nilai piksel dalam rentang yang valid.
'''