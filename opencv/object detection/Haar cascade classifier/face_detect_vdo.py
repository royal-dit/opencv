import cv2
cap = cv2.VideoCapture("object detection\images\WIN_20230125_19_50_47_Pro.mp4")
face_cascade = cv2.CascadeClassifier("object detection\Haar cascade classifier\haarcascade_frontalface_default.xml")


while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#return 4 values for rectangle
    faces = face_cascade.detectMultiScale(gray,1.2,8,minSize=(30,30))  #here 1.2 is scale factor and 5 is minneighbours

    for (x,y,w,h) in faces:
         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("frame",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
