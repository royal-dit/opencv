#mean shift object tracking  
#locating the moving object over time

import cv2
import numpy as np
cap = cv2.VideoCapture("object detection\images\Screen Recording (1-25-2023 11-01-38 PM).mp4")
#take th first frame of image
ret,frame = cap.read()

#set the initail location of window
x,y,width,height = 600,350,90,80
track_window = (x,y,width,height)

#set up the roi for tracking
region_of_interest = frame[y:y+height,x:x+width]

#converting to hsv color channel
hsv = cv2.cvtColor(region_of_interest,cv2.COLOR_BGR2HSV)

#for histogram only hue is consider so we do inrange func
mask = cv2.inRange(hsv,np.array((0.,60.,32.)),np.array((180.,255.,255.)))

roi_hist = cv2.calcHist([hsv],[0],mask,[180],[0,180])

cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)


#setup the termination criteria either 10 iteration or move by atleast 1 pt
#histogram back projection
term_crit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT,10,1)


cv2.imshow("roi",region_of_interest)

while True:
    res,frame = cap.read()
    if res == True:
        hsvv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #this gives the back projected image
        dst = cv2.calcBackProject([hsvv],[0],roi_hist,[0,180],1)
        
        #apply meanshift to get new location
        ret,track_window = cv2.meanShift(dst,track_window,term_crit)
        
        #draw it on image
        x,y,w,h = track_window
        
        final_image = cv2.rectangle(frame,(x,y),(x+w,y+h),255,1)
        
   
    
    cv2.imshow("frame",final_image)
    cv2.imshow("back_projected",dst)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()