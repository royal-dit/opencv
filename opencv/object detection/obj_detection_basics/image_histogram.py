#histogram of an image
#contrast brightness insensity



import numpy as np
import cv2
import matplotlib.pyplot as  plt
img = cv2.imread("object detection\obj_detection_basics\pizza.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

b,g,r = cv2.split(img)


# img = np.zeros((200,200),np.uint8)
# cv2.rectangle(img,(0,100),(200,200),(255,255,255),-1)
# cv2.rectangle(img,(0,50),(100,100),(127),-1)


cv2.imshow("img",img)

cv2.imshow("b",b)


cv2.imshow("g",g)


cv2.imshow("r",r)


#finds the pixel intensity or pixel value intesity 
plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()