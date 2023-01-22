#Image pyramid with python 
#create the images of diffirent resolution
import cv2
import numpy as np
img = cv2.imread("object detection\EdgeDetection\Lenna.png")
img = cv2.resize(img,(500,500))
                   #gaussian pyramid
lr = cv2.pyrDown(img)
lr2 =cv2.pyrDown(lr)
#increase resolution
hr2 = cv2.pyrUp(lr2)

# cv2.imshow("image1",img)
cv2.imshow("image2",lr)
# cv2.imshow("image3",lr2)
cv2.imshow("images3",hr2)


                         #
#this code decresease resolution of same image for 5 times
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)


#laplacian pyramid is formed by the diffirence between that level in gaussian pyramin and expnaded pyramid
#its is also used as edge detection

layer = gp[5]
cv2.imshow("upper level gaussioan pyramid",layer)
lp= [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)
    
       

cv2.waitKey(5000)
cv2.destroyAllWindows()

