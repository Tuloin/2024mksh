# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:01:53 2024

@author: USER
"""
import cv2
img = cv2.imread("onepiece.png.png")
b=img[:,:,0] #藍色
g=img[:,:,1] #綠色
r=img[:,:,2] #紅色

img_rbb=cv2.merge([r,b,b])
cv2.imwrite("rbb.png",img_rbb)
cv2.imshow("RBB",img_rbb)
cv2.imshow("opencv02",img)
cv2.waitKey(0)

#如果按下任意鍵,會把全部的視窗都關閉
cv2.destroyAllWindows()