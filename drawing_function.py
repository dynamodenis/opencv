import cv2

img = cv2.imread('comps.png', 1)

img = cv2.line(img,(0,0),(640,480),(200,45,78),10)
img = cv2.arrowedLine(img,(50,50),(640,480),(56,45,78),10)

cv2.imshow('images',img)

cv2.waitKey(0) 
# conditional to estroy window without saving image
cv2.destroyAllWindows()