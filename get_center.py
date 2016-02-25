# -*- coding: utf-8 -*-
'''
Get center of gravity that red and green area
'''
import cv2
import math
import numpy as np
import sys
import traceback
import serial
import time

def squ(x):
    return x*x

def maxlist(cnt):
    max_num=0
    for i in range(len(cnt)):
        cnt_num=len(cnt[i])
        if cnt_num>max_num:
            max_num=cnt_num
            max_i=i
    return max_i

cv2.namedWindow("src")
cv2.namedWindow("r")
cv2.namedWindow("g")
cap = cv2.VideoCapture(0)
count = 0
kernel = np.ones((5,5),np.uint8)

#com_n = 4
#ser = serial.Serial(com_n-1,9600,timeout = 1)

rmin = np.array([160,100,100])
rmax = np.array([190,255,255])
gmin = np.array([40,100,20])
gmax = np.array([70,255,255])

while 1:
    try:
        ret, img_src = cap.read()
        #img_src = cv2.resize(img_src,(img_src.shape[1]/2,img_src.shape[0]/2))
        img_hsv = cv2.cvtColor(img_src,cv2.COLOR_BGR2HSV)
        #masking red and green area
        maskr = cv2.inRange(img_hsv,rmin,rmax)
        maskg = cv2.inRange(img_hsv,gmin,gmax)
        #noise reduction
        for i in range(1):        
                        
            maskr = cv2.medianBlur(maskr,5)
            maskg = cv2.medianBlur(maskg,5)
        for i in range(1):
            pass
            #maskr = cv2.morphologyEx(maskr,cv2.MORPH_OPEN,kernel)
            #maskg = cv2.morphologyEx(maskg,cv2.MORPH_OPEN,kernel)
            #maskr = cv2.morphologyEx(maskr,cv2.MORPH_CLOSE,kernel)
            #maskg = cv2.morphologyEx(maskg,cv2.MORPH_CLOSE,kernel)
        
        #cntr = cv2.findContours(maskr,1,2)[0] #extract outline
        #cntg = cv2.findContours(maskg,1,2)[0]
        #ri = maxlist(cntr)
        #gi = maxlist(cntg)
        #get center of gravity
        Mr = cv2.moments(maskr)
        Mg = cv2.moments(maskg)
        rx = int(Mr["m10"]/Mr["m00"])
        ry = int(Mr["m01"]/Mr["m00"])
        gx = int(Mg["m10"]/Mg["m00"])
        gy = int(Mg["m01"]/Mg["m00"])
        #get their center
        cx = (rx+gx)/2
        cy = (ry+gy)/2
        
        m = (ry-gy)/(rx-gx)
        #ser.write(str(m))
        #time.sleep(0.1)
        #arduinom = ser.readline()
        
        ran = math.sqrt(squ(rx-gx)+squ(ry-gy))
        #ser.write(str(ran))
        #time.sleep(0.5)
        #arduinoran = ser.readline()
        
        print str(m) +" , " +str(ran) #str(cx) +","+str(cy)
        #print "arduino:",
        #print arduinom
        dstr = cv2.bitwise_and(img_src,img_src,mask=maskr)
        dstg = cv2.bitwise_and(img_src,img_src,mask=maskg)
        
        cv2.circle(img_src,(rx,ry),5, (0,0,255), -1)
        cv2.circle(img_src,(gx,gy),5, (0,255,0), -1)
        cv2.circle(img_src,(cx,cy),5, (255,255,255),-1)
        
        cv2.imshow("src",img_src)
        cv2.imshow("r",dstr)
        cv2.imshow("g",maskg)
        
        ch = cv2.waitKey(1)
        if ch == ord("q"):
            break
        count = 0

    except:
        print "error"
        cv2.imshow("src",img_src)
        #count += 1
        ch = cv2.waitKey(1)
        if ch == ord("q"):
            print "____________________________________________"
            print traceback.format_exc(sys.exc_info()[2])
            print "____________________________________________"
            break
    
cap.release()
cv2.destroyAllWindows()
#ser.close()
