#simple image Thresholding spereating a object from background
# import cv2
import cv2
# img = cv2.imread("object detection/gradient.jpg",0)
# img = cv2.resize(img,(500,500))
# # if the val is greater than 127 then it is assign to 1 and less than 127 is assigned too 0
# _,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# _,th2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
# _,th3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)
# cv2.imshow("Image",img)
# cv2.imshow("Th1",th1)
# cv2.imshow("Th2",th2)
# cv2.imshow("Th3",th3)


#adaptive threshold
img2 = cv2.imread("object detection/pizza.jpg",0)

th4 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
img2 = cv2.resize(img2,(500,500))
th4 = cv2.resize(th4,(500,500))
cv2.imshow("image2",img2)
cv2.imshow("image1",th4)
cv2.waitKey(50000)
cv2.destroyAllWindows()


