#video object tracking 
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def nothing(x):
    pass
#create a new tracking window
cv2.namedWindow("Tracking")
#created tracker can then be used to track an object in a video
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    re,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # getTrackbarPos retrieve the current position of an object being tracked by a created Tracker 
    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_S = cv2.getTrackbarPos("LS","Tracking")
    l_V = cv2.getTrackbarPos("LV","Tracking")
    
    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")
    
    l_b = np.array([l_h,l_S,l_V])
    u_b = np.array([u_h,u_s,u_v])
    # filter an image based on a specified range of pixel values.
    #but only pixels that fall within the specified range of values are present in the output image
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    if re == True:
        cv2.imshow('frame',frame)
        cv2.imshow('frame1',mask)
        cv2.imshow('frame2',res)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
cap.release
cv2.destroyAllWindows()
    