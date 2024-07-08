import cv2

img=cv2.imread("onepiece.png.png")
#讀入opencv.png這張圖,小心副檔名
cv2.imshow("one",img)#要在"one"秀圖
cv2.imshow("ya",img)
cv2.imshow("ruru",img)
cv2.waitKey(0)#等待任意見,卡住,不要結束
#如果沒圖執行會當掉
#另存新檔 opencv01.py
#存在「桌面」的opencv01.py
#圖也要放在同一個目錄「桌面」