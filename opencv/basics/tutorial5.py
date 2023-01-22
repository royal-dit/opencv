#setting date and time on video
import cv2
import datetime
cap = cv2.VideoCapture(0)
cap.set(3,300)
cap.set(4,400)
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        #sets height and width on video 
        text = "Width:"+str(cap.get(3))+"Height:"+str(cap.get(4))
        
        #set date and time in video
        datet = str(datetime.datetime.now())
        
        frame = cv2.putText(frame,datet,(30,30),font,0.6,(255,255,8),1,cv2.LINE_AA)  
        cv2.imshow('vid',frame)
        if cv2.waitKey(1)& 0xFF==ord("q"):
            break
cap.release
cv2.destroyAllWindows()

    