import cv2

img = cv2.imread("RGB.jpg")
img =cv2.resize(img,(300,256))
img1 = cv2.applyColorMap(img,cv2.COLORMAP_BONE)
img2 = cv2.applyColorMap(img,cv2.COLORMAP_OCEAN)
img3 = cv2.applyColorMap(img,cv2.COLORMAP_COOL)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)

cv2.waitKey(0)

cv2.destroyAllWindows()