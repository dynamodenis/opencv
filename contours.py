import cv2
import numpy as np



# this diaplay an image
img = cv2.imread('me.jpg')
# turn it to gray
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# set the threshold
ret , threshold = cv2.threshold(grayimg, 127, 200, 0)
contours, hierarcy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# now draw contours on the original img
cv2.drawContours(img, contours, -1, (0,200,50),3)


cv2.imshow('image',img)
cv2.imshow('imagegray',grayimg)

    
cv2.waitKey(0)
cv2.destroyAllWindows()