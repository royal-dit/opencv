#Draw geometric shapes on images using Python OpenCV
import cv2
import numpy as np
img = cv2.imread("cat.jpg",0)

#code to draw line in a image
img= cv2.line(img,pt1=(0,0),pt2=(255,255),color=(0,255,255),thickness=5)

#code to  draw arrow line in image
img = cv2.arrowedLine(img,(0,0),(100,100),(255,0,0),10)

#Draw rectange in the image
img = cv2.rectangle(img,(0,0),(100,100),(255,0,0),4)

#draw circle in the image
img = cv2.circle(img,(120,120),10,(255,150,100),6)

#code to put text in the image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"Royal Dahal",(50,50),font,2,(255,255,200),6,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(500)
cv2.destroyAllWindows()


                    #creating a image using numpy 
img_np = np.zeros((500,500,3),dtype=np.uint8)
img_np[:] = (255,255,255)

#draw balck line
img_np =cv2.line(img_np,(0,0),(100,100),(0,0,155),5)
#draw arrow
img_np = cv2.arrowedLine(img_np,(0,0),(100,100),(0,0,155),5)
#draw circle
img_np = cv2.circle(img_np,(120,120),20,(255,124,234),5)


cv2.imshow("image",img_np)
cv2.waitKey(5000)
cv2.destroyAllWindows()



