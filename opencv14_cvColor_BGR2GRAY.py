# -*- coding: utf-8 -*-
import cv2
img = cv2.imread("Lena.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("open14",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()