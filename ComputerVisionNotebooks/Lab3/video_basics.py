import cv2 
cam = cv2.VideoCapture(1)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

import time
time.sleep(2)

while True:
    ret, frame = cam.read()
    
    if not ret:
        print('Error in retrievng frame. Existing...')
        break
    if frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow("Camera" , frame)
    else:
        print("Error: Invalid Dimensions")
        
    if cv2.waitKey(1) == ord('q'):
        break

    
cam.release()
cv2.destroyAllWindows()
    