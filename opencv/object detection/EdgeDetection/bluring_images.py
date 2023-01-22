import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("object detection/pizza.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


#decleearing kernel  1/k_h * k_w
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)


blur  = cv2.blur(img,(5,5));

#gaussian filter algorithms 
#gf is nothing but using diffirent-weight-kernel in both x and y direction
gauss_blur = cv2.GaussianBlur(img,(5,5),0)


#median filter  is best for salt and papper dot images 
#mf is something that  each pixel value with the median of its neighbouting pixels.this method is great when dealing ith salt and pepper noise
med_blur = cv2.medianBlur(img,5)

#bileteral filter is best for preserving edges in images 
bil_filter = cv2.bilateralFilter(img,9,75,75)


titles = ["image","2D convo","blur","gaussian blur","med_blur","bileteral filter"]
images = [img,dst,blur,gauss_blur,med_blur,bil_filter]

#lpf helps in removing noises bluring the images 
#hpf filters helps in finding edges in the images 



for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()