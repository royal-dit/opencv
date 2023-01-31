#shi Tomasi corner detection 
import numpy as np 
import cv2 
img = cv2.imread("object detection\images\suduko.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,maxCorners=500, #maximum numbers of corners to show
                                  qualityLevel=0.01,
                                  minDistance=10 )#is the mininmum possible euclidean distance btn corner

corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),radius=3,color=255,thickness=-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()