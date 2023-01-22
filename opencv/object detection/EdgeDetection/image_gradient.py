#image gradient  and edge detection
#an image gradient is a directional change in the intesity or color in an image
import cv2 
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread("object detection/suduko.png",cv2.IMREAD_GRAYSCALE)

#laplacian method to find out laplacian gradient of image
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

#sobelX change in direction in intensity is in X axis
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelx = np.uint8(np.absolute(sobelx))

#sobely change in direction in intensity is in y axis
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobely = np.uint8(np.absolute(sobely))

#sobel combine
sobelCombined  = cv2.bitwise_or(sobelx,sobely)





titles = ["image","laplacian gradient","sobelx","sobely","sobel combined"]
images = [img,lap,sobelx,sobely,sobelCombined]
for i in range(4):
    plt.subplot(2,3,i+1)
    
    plt.imshow(images[i],'gray')
    plt.title(titles[i])


plt.show()


