#find and draw contours  vvi

import cv2
img = cv2.imread("object detection/EdgeDetection/lenna.png")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh = cv2.bitwise_not(imgray)  #invert black to white and white to black
ret ,thresh = cv2.threshold(imgray,100,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("number of contours:"+str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,240),2)


cv2.imshow("image",img)
cv2.imshow("image_Gray",imgray )

cv2.waitKey(0)
cv2.destroyAllWindows()

