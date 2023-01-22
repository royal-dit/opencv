#reigion of interest
import cv2
img = cv2.imread("cat.jpg")
print(img.shape)
b,g,r = cv2.split(img)

cat_lg = img[100:150,150:200]
img[110:140,90:130] = cat_lg

cv2.imshow("image",img)
if cv2.waitKey(0) & 0xFF==ord('q'):
     cv2.destroyAllWindows()

