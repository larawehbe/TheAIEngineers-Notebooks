import cv2
import numpy as np

# Load the pre-trained classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Read the image
img = cv2.imread('path_to_your_image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Region of Interest (ROI) for face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Detect eyes within the face ROI
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    for (ex,ey,ew,eh) in eyes:
        # Draw rectangle around eyes
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# Display the result
cv2.imshow('Eye Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()