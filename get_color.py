#_*_coding: utf-8 _*_

import cv2
import math
import numpy as np
import sys
import traceback

def squ(x):
    return x*x

cv2.namedWindow("src")
cv2.namedWindow("r")
cv2.namedWindow("g")
cap = cv2.VideoCapture(1)
count = 0
kernel = np.ones((5,5),np.uint8)
rmin = np.array([160,100,0])
rmax = np.array([190,255,255])
gmin = np.array([40,150,0])
gmax = np.array([70,255,255])
while 1:
    try:
        ret, img_src = cap.read()
        #img_src = cv2.resize(img_src,(img_src.shape[1]/2,img_src.shape[0]/2))
        img_hsv = cv2.cvtColor(img_src,cv2.COLOR_BGR2HSV)
        maskr = cv2.inRange(img_hsv,rmin,rmax)
        maskg = cv2.inRange(img_hsv,gmin,gmax)
        maskr = cv2.medianBlur(maskr,3)
        maskg = cv2.medianBlur(maskg,3)
        for i in range(5):
            maskr = cv2.morphologyEx(maskr,cv2.MORPH_OPEN,kernel)
            maskg = cv2.morphologyEx(maskg,cv2.MORPH_OPEN,kernel)
            #maskr = cv2.morphologyEx(maskr,cv2.MORPH_CLOSE,kernel)
            #maskg = cv2.morphologyEx(maskg,cv2.MORPH_CLOSE,kernel)
        #img_dst = cv2.bitwise_and(img_src,img_src,mask=maskg)
        #cnt = cv2.findContours(maskg,1,2)[0][0]
        Mr = cv2.moments(maskr)
        Mg = cv2.moments(maskg)
        rx = int(Mr["m10"]/Mr["m00"])
        ry = int(Mr["m01"]/Mr["m00"])
        gx = int(Mg["m10"]/Mg["m00"])
        gy = int(Mg["m01"]/Mg["m00"])
        cx = (rx+gx)/2
        cy = (ry+gy)/2
        m = (ry-gy)/(rx-gx)
        ran = math.sqrt(squ(rx-gx)+squ(ry-gy))
        print str(m) +"," +str(ran) #str(cx) +","+str(cy)
        cv2.circle(img_src,(rx,ry),5, (0,0,255), -1)
        cv2.circle(img_src,(gx,gy),5, (0,255,0), -1)
        cv2.circle(img_src,(cx,cy),5, (255,255,255),-1)
        cv2.imshow("src",img_src)
        cv2.imshow("r",maskr)
        cv2.imshow("g",maskg)
        ch = cv2.waitKey(1)
        if ch == ord("q"):
            break
        count = 0
    except:
        print "error"
        count += 1
        if count > 100:
            print "____________________________________________"
            print traceback.format_exc(sys.exc_info()[2])
            print "____________________________________________"
            break

cap.release()
cv2.destroyAllWindows()