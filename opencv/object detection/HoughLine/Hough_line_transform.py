#hough line tansformation(The standard hough transform)
import cv2
import  numpy as np
img = cv2.imread("object detection\images\suduko.png")
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,150,150,apertureSize=3)


# rho is the distance resolution of the acc in pixels 
#theta angle resoln of acc in radians
# threshold accumulator threshold parameter only those line are returned that get enough votes
lines = cv2.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    
    r,theta = line[0]  #rho is the distance from the coordinate top left,  theta is line roatition angle in radian s
    a = np.cos(theta)
    b = np.sin(theta)
    
    x0 = a*r
    y0 = b*r
    
    #x1 stores the rounded off value of (r*cos(theta)-1000*sin(theta))
    x1 = int(x0+1000 * (-b))
    
    #y1 stores the rounded off value of (r*sin(theta)+1000*cos(theta))
    y1 = int(y0+1000 * (a))
    
    #x2 stores the rounded off value of (r*cos0+100*sin0)
    x2 = int(x0+1000 * (-b))
    
    #y2 stores the rounded off value of (r*sin0-1000*cos0)
    y2 = int(y0-1000 * (a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
    
cv2.imshow("img",img)
cv2.imshow("img2",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

