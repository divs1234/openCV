import numpy as np
import cv2
import math

cap = cv2.VideoCapture(0)
i=0
while(i<360):
    ret, frame = cap.read()

    cols=cap.get(3)
    rows=cap.get(4)
    i=i+1
    
    M = np.float32([[math.cos(math.pi/i),-math.sin(math.pi/i),0],[math.sin(math.pi/i),math.cos(math.pi/i),0]])
    dst = cv2.warpAffine(frame,M,(int(cols),int(rows)))
    
    cv2.imshow('frame',dst)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
