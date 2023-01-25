#face detection using haar feature based cascde classifier

import cv2

face_cascade = cv2.CascadeClassifier("object detection\Haar cascade classifier\haarcascade_frontalface_default.xml")

img = cv2.imread("object detection\images\lena.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#return 4 values for rectangle
faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
cv2.imshow("img",img)
cv2.waitKey()