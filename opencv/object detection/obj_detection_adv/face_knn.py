import numpy as np 
import cv2
import os
from sklearn.neighbors import KNeighborsClassifier

#implement knn
def knn(train,test):
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(train)




cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("object detection\obj_detection_adv\haarcascade_frontalface_alt.xml")
dataset_path = "./object detection/obj_detection_adv/face_dataset/"

face_data = []
labels = []
class_id = 0 #labels for every given file 
names = {} #mapping between id and name

#dataset preperation
for fx in os.listdir(dataset_path): #looping through every file in the folder
    if fx.endswith('.npy'):  #checking .npy extension in file
        names[class_id] = fx[:4] #.npy are last 4 indices so we are taking name only
        data_item = np.load(dataset_path+fx)
        face_data.append(data_item)
        target  = class_id * np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)


face_dataset = np.concatenate(face_data,axis=0)
face_labels = np.concatenate(labels,axis=0).reshape((-1,1))
print(face_labels.shape)
print(face_dataset.shape)


trainset = np.concatenate((face_dataset,face_labels),axis = 1)
print(trainset.shape)


font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    
    for face in faces:
        x,y,w,h = face
        offset = 5
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section,(100,100))
        
        
        #use knn here
        out = knn(trainset,face_section.flatten())
        
        
        #draw rectangle in the original image
        cv2.putText(frame,names[int(out)],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imshow("faces",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

        