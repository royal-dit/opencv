#read and write images using cv2
import cv2
img = cv2.imread("cat.jpg",1)
cv2.imshow('image',img)
ke = cv2.waitKey(5000)
if ke == 27:   #if pressed esc key it will destroy window
    cv2.destroyAllWindows()
elif ke ==ord('s'):  #if s is pressed then the image will be saved 
    cv2.imwrite("cat_copy.jpg",img)



