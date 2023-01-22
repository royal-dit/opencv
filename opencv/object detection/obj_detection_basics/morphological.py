import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread("object detection/smarties.jpg",cv2.IMREAD_GRAYSCALE)

_,mask = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=10)
erosion = cv2.erode(mask,kernel,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)


titles = ["image","mask","dilation","erosion","opening","closing","mg"]
images = [img,mask,dilation,erosion,opening,closing,mg]

for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()