import cv2

# Gausian Pyramid
img = cv2.imread('comps.png')
# make image smaller
lr = cv2.pyrDown(img)
# make the image even more smaller
lr2 = cv2.pyrDown(lr)
# start increasing the image
hr2 = cv2.pyrUp(lr2)


cv2.imshow('original',img)
cv2.imshow('lower1',lr)
cv2.imshow('lower2',lr2)
cv2.imshow('pyrUp2',hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()