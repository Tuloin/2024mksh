import cv2
img = cv2.imread("doll.jpg")
img = cv2.resize(img,(320,240))
cv2.imshow("open12",img)

b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

m=0
for i in [b,g,r]:
    for k in [b,g,r]:
        for l in [b,g,r]:
            d=cv2.merge([i,k,l])
            cv2.imshow("RGB"+str(m),d)
            cv2.moveWindow("RGB"+str(m),m//6*200,m%6*200)
            m +=1
            cv2.waitKey(330)
cv2.waitKey(0)
cv2.destroyAllWindows()