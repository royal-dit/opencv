#road lane detection in image
import cv2
import matplotlib.pyplot as plt
import numpy as np
 
cap = cv2.VideoCapture("object detection\HoughLine\lane video.mp4")

def process(img):
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    #taking our region of interest 
    region_of_interest = [(120,height),(width/1.6,height/1.8),(width/1.3,height)]

    def roi(img,vertices):
        mask = np.zeros_like(img)   #creating matrix same of orginal image
        #channel_count = img.shape[2]  #counting the channels 
        #match_mask_color = (255,) * channel_count   #this is fro color image

        match_mask_color = 255  #this is for gray scale
        cv2.fillPoly(mask,vertices,match_mask_color) #fills the unwanted region
        masked_image = cv2.bitwise_and(img,mask)
        return masked_image


    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_img,100,120,apertureSize=3)
    cropped_image = roi(canny_image,np.array([region_of_interest],np.int32))
    lines = cv2.HoughLinesP(cropped_image,
                            rho = 3,
                            theta =np.pi/180,
                            threshold=160,
                            lines=np.array([]),
                            minLineLength=100,
                            maxLineGap=50)

    #creating a blank image 
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype = np.uint8)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),3)

    #merging the orginal and  line drawn blank image   
    img2= cv2.addWeighted(img,0.8,blank_image,1,0.0)   
    return img2


while True:
    ret,frame = cap.read()
    frame = process(frame)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
