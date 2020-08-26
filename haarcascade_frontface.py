import cv2
import numpy as np

#Load Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# load image
# img = cv2.imread('me.jpg')
# load video
cap = cv2.VideoCapture('webcam.webm')

while cap.isOpened():
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),3)


    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.destroyAllWindows()
    
cap.release()