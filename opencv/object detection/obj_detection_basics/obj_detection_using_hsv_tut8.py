#objection detection using hsv color space
#hue value and saturation

import cv2
import numpy as np
def nothing(x):
    pass

#creating a track bar to adjsut lower and upperbound of hsv color
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    frame = cv2.imread('smarties.jpg')
    frame = cv2.resize(frame,(500,500))
    #converting rgb to hsv color channel
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #getiing the value of hsv using tracking
    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_s = cv2.getTrackbarPos("LS","Tracking")
    l_v = cv2.getTrackbarPos("LV","Tracking")
    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")
    
    #getting the value of lower blue and upper blue
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("frame1",mask)
    cv2.imshow("frame2",res)
    key = cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()