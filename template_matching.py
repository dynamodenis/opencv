import cv2
import numpy as np

#histogram is the graphical representation of an image
# img = np.zeros((200,200), np.uint8)
# cv2.rectangle(img,(0,100), (200,200),200,-1)

img = cv2.imread('me.jpg')
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('doha.jpg',0)

w,h= template.shape[::-1]

res = cv2.matchTemplate(grayimg, template, cv2.TM_CCOEFF_NORMED)
##print(res)

threshold = 0.1;
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w, pt[1]+h), (0,255,0),3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()