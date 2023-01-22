#canny edge detector is an edge detection operator that uses a multi stage algorithm to detect a wide range of edges in images.
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("object detection/smarties.jpg")
#steps 
# 1 noise reduction
#2 gradient calculation
#non maximum supression
#double threshold
#edge tracking by hysteresis

canny = cv2.Canny(img,100,200)

titles = ["images","canny"]
images = [img,canny]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
