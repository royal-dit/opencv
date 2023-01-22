#capturing  live images and videos
import cv2
cap = cv2.VideoCapture(0) #captures the video 

#code for saving the readed video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi',-fourcc,20.0,(640,480))

# while(cap.isOpened):
while(True):
    ret,frame = cap.read() #capture frame 
    
    if ret==True:
        #give tge height and width of frame
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        
        output.write(frame) 
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # convert the frame into grayscale
        cv2.imshow('frame',frame)  #show the grayscale image 
        
    if cv2.waitKey(1) & 0xFF==ord('q'):  #if pressed q the frame will break
        break
    
cap.release()
cv2.destroyAllWindows()

        
    