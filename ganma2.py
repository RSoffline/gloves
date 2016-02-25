# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

cv2.namedWindow("src")
cv2.namedWindow("dst")
cap = cv2.VideoCapture(0)

y = np.ones((256,1),dtype = "uint8")
for i in range(255):
    #y[i][0] = 255*pow(float(i)/255,1.0/2.0)
    y[i][0] = 255-i
#np.sin(y[0,255][0])
while 1:
    ret, img_src = cap.read()
    #img_bgr = cv2.split(img_src)
    #img_bgr[2] = cv2.LUT(img_bgr[2],y)
    #img_dst = cv2.merge(img_bgr)
    #img_dst = cv2.LUT(img_src,y)
    img_dst = cv2.cvtColor(img_src,cv2.COLOR_BGR2HSV)    
    cv2.imshow("src",img_src)
    cv2.imshow("dst",img_dst)
    ch = cv2.waitKey(1)
    if ch == ord("q"):
        break
cv2.destroyAllWindows()