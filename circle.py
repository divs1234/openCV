import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
i=0
while(i==0):
    #i=1+1
    ret,image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    #output = image.copy()
    cv2.imshow("output", image)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,20,80,60,20,20)
    #print(circles)
    if circles is not None:
        circles = np.int32(circles[0, :])
        print(circles)
        if [80] in circles: continue
        for [x, y, r] in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 1)            
        cv2.imshow("output", image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.wait(1)
cv2.destroyAllWindows()
