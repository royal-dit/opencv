#find and draw contours 
import cv2
img = cv2.imread("object detection/EdgeDetection/lenna.png")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret ,thresh = cv2.threshold(imgray,100,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("number of contours:"+str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,240),2)


cv2.imshow("image",img)
cv2.imshow("image_Gray",imgray )

cv2.waitKey(0)
cv2.destroyAllWindows()

