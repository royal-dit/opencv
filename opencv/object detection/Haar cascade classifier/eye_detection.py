#eye detection using haar cascade
import cv2
import numpy as np

cap = cv2.VideoCapture("object detection\images\WIN_20230125_19_50_47_Pro.mp4")
glasses = cv2.imread("object detection\images\png-clipart-sunglasses-eyewear-glasses-black-glasses-thumbnail.png")
eye_cascade = cv2.CascadeClassifier("object detection\Haar cascade classifier\haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier("object detection\Haar cascade classifier\haarcascade_frontalface_default.xml") 
while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,6)
  
    for (x,y,w,h) in faces:
        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w] #gives grayscale region of interest
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            # Resize the glasses image to match the size of the eyes
            glasses = cv2.resize(glasses, (ew, eh))
            
            # Get the region of interest (ROI) for the eyes
            roi_eye = img[y+ey:y+ey+eh, x+ex:x+ex+ew]
            
            # Create a mask for the glasses
            gw = glasses.shape[0]
            gh = glasses.shape[1]
            gc = glasses.shape[2]
            mask = np.zeros((gw, gh), dtype=np.uint8)
            mask[:,:] = (glasses[:,:,2] != 0)
            
            # Get the background of the ROI
            roi_bg = cv2.bitwise_and(roi_eye, roi_eye, mask=cv2.bitwise_not(mask))
            
            # Get the foreground of the glasses
            roi_fg = cv2.bitwise_and(glasses[:,:,:3], glasses[:,:,:3], mask=mask)
            
            # Combine the background and foreground
            roi_eye = cv2.add(roi_bg, roi_fg)
            
            # Update the ROI in the original image
            img[y+ey:y+ey+eh, x+ex:x+ex+ew] = roi_eye
                
            
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    