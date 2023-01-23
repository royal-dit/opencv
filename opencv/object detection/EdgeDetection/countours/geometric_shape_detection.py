#detect simple geometric shape using open cv
import cv2
img = cv2.imread("object detection\EdgeDetection\contours(vvi)\shape.png")
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(imgGrey,100,255,cv2.THRESH_BINARY)
contours ,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(255,200,100),4)
    #find the x and y coordinate
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    
    elif len(approx)==4:
        x,y,w,h =cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img,"Square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))   
        else: 
          cv2.putText(img,"rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
        
    else:
        cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        




cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

