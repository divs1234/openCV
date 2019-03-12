import numpy as np
import math as mt
import cv2

cap=cv2.VideoCapture(0)
i=0
rows=cap.get(3)
cols=cap.get(4)
while(i<100):
    ret, frame= cap.read()
    M = np.float32([[1,0,i],[0,1,i]])
    
    i=i+0.1
    sfd=cv2.warpAffine(frame,M,(int(rows),int(cols)))
    resize_img = cv2.resize(frame , (int(cols)*2 , int(rows)*2))
    cv2.imshow('frame',resize_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
