#handle mouse event in open cv
import cv2
import numpy as np
events = [i for i in dir(cv2) if 'EVENT' in i]

def click_event(event,x,y,flags,param):
    #print the axis in the image where we click from the mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ','+ str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(255,234,234),1,cv2.LINE_AA)
        cv2.imshow('image',img)
   
    #print the color channel  in the image where we click from the 
    if event == cv2.EVENT_RBUTTONDOWN:
            blue = img[y,x,0]
            green = img[y,x,0]
            red = img[y,x,2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            strrbg = str(blue) + ','+ str(green)+','+str(red)
            cv2.putText(img,strrbg,(x,y),font,0.5,(255,234,234),1,cv2.LINE_AA)
            cv2.imshow('image',img)
            
img = np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)        
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()