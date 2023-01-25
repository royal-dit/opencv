import numpy as np
import cv2
img = cv2.imread("object detection\images\shape.png")
output = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray  = cv2.medianBlur(gray,5)
circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

detected_circles = np.uint16(np.around(circle))

for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),2)
    cv2.circle(output,(x,y),2,(0,255,255),3)

cv2.imshow("image",output)
cv2.waitKey(0)
cv2.destroyAllWindows()