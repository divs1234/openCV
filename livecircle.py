import cv2
import numpy as np

img1 = cv2.imread('trial.jpg',3)
cv2.imshow('circles',img1)
img = cv2.medianBlur(img1,5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1, 20,20,60,40,100)

circles = np.uint16(np.around(circles))
print(circles)
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img1,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
