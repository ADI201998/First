import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    t = 0
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lg = np.array([30,120,10])
    ug = np.array([40,255,255])
    mask1 =  cv2.inRange(hsv, lg, ug)
    cv2.imshow('frame1',mask1)
    gauss = cv2.GaussianBlur(mask1,(7,7),0)
    gauss = cv2.GaussianBlur(gauss,(3,3),0)
    canny = cv2.Canny(gauss,300,500)
    kernel = np.ones((35,35),np.uint8)
    dilate = cv2.dilate(canny,kernel,iterations = 2)
    kernel1 = np.ones((21,21),np.uint8)
    erode = cv2.erode(dilate,kernel1,iterations = 2)
    cv2.imshow('frame3',erode)
    im2,contours,hierarchy = cv2.findContours(erode,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        r = (cv2.contourArea(cnt)/np.pi)**0.5
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        ro = max(w,h)
        area2 = (ro*ro*np.pi)/4
        #area1 = w*h
        #area2 = 4*(r**2)
        if (area/area2) > 0.99 and cv2.contourArea(cnt)>2000:
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame,(cx,cy), int(r), (0,0,255), 3)
            cv2.imshow('ball',frame)
            break
        else:
            cv2.imshow('ball',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
