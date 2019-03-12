import cv2

img = cv2.imread('trial.jpg' , 0)

cv2.imshow('img' , img)

resize_img = cv2.resize(img  , (28 , 28))
cv2.imshow('img' , resize_img)
x = cv2.waitKey(0)
if x == 27:
    cv2.destroyWindow('img')
