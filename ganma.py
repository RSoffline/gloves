# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

cv2.namedWindow("src")
cv2.namedWindow("dst")
cap = cv2.VideoCapture(0)

while 1:
    ret, img_src = cap.read()
    
    img_bgr = cv2.split(img_src)
    img_dst = cv2.merge((img_bgr[2],img_bgr[0],img_bgr[1]))
  
    cv2.imshow("src",img_src)
    cv2.imshow("dst",img_dst)
    ch = cv2.waitKey(1)
    if ch==ord("q"):
        break

cv2.destroyAllWindows()


