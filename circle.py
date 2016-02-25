# -*- coding: utf-8 -*-
import cv2
import numpy as np

cv2.namedWindow("src")
cv2.namedWindow("dst")
cap=cv2.VideoCapture(0)
count = 0
rmin = np.array([0,0,0])
rmax = np.array([179,255,127])
while 1:
    try:
        ret, img_src=cap.read()
        count += 1
        #cv2.circle(img_src,(130,400),30,(0,255,255),-1)
        img_hsv = cv2.cvtColor(img_src,cv2.COLOR_BGR2HSV)
        img_ran = cv2.inRange(img_src,rmin,rmax)
        img_dst = cv2.bitwise_and(img_src,img_src,mask=img_ran)
        cv2.imshow("src",img_src)
        cv2.imshow("dst",img_dst)
        if count == 600:
            count = 0
        ch = cv2.waitKey(1)
        if ch == ord("q"):
            break
    except:
        print "error"
        ch = cv2.waitKey(1)
        if ch == ord("q"):
            break
cv2.destroyAllWindows()
cap.release()