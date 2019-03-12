import cv2
import numpy as np
import math

img = cv2.imread('trial.jpg',0)
rows,cols = img.shape

M = np.float32([[math.cos(math.pi/6),-math.sin(math.pi/6),0],[math.sin(math.pi/6),math.cos(math.pi/6),0]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
