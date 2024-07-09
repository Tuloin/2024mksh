import cv2

img=cv2.imread("mksh.jpg")
b=img[:,:,0]#藍色的channel
print(b)
cv2.imshow("opencv06",img)
cv2.waitKey(3000)
#等3秒鐘，都沒按鍵，就離開
cv2.destroyAllWindows()

