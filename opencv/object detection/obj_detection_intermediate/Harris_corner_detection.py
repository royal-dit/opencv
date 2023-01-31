#detect the corner using the harris corner detection
import cv2
import numpy as np 
img = cv2.imread("object detection\images\suduko.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
hcd = cv2.cornerHarris(gray,blockSize=2,ksize=3,k=0.04)

#expand the object in the image making it bigger and thicker
hcd = cv2.dilate(hcd,None)

#giving the threshold value
img[hcd>0.01 * hcd.max()] = [0,0,255]
cv2.imshow("hcd",img)
cv2.waitKey(0)
cv2.destroyAllWindows

