import cv2
import numpy as np

# Load the pre-trained classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img = cv2.imread("../DATA/Nadia_Murad.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray,1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y) , (x+w,y+h), (255,0,0), 2)
    
    
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.8)
    
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey) , (ew+ex, ey+eh) , (0,255,0), 2 )
    
    
cv2.imshow('Eye Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()