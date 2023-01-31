#separate an object from its background in a video stream
# MOG (Mixture of Gaussians)
# MOG2 (Improved Mixture of Gaussians)
# GMG (Gradient Masked Mixture of Gaussians)
# KNN (K-Nearest Neighbors)
import cv2
cap = cv2.VideoCapture("object detection\images\People Walking Free Stock Footage, Royalty-Free No Copyright Content.mp4")

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#   1st method
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()


#   2nd method
#detects shadow too
# a = cv2.createBackgroundSubtractorMOG2()


#   3rd method
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

# 4th method
fgbg = cv2.createBackgroundSubtractorKNN()


while True:
    _,frame = cap.read()
    #getting the foreground mask
    fgmask = fgbg.apply(frame)
    # fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel) only of gmg
    cv2.imshow("frame",fgmask)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
