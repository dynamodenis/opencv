from matplotlib import pyplot as plt
import cv2
import numpy as np

#histogram is the graphical representation of an image
# img = np.zeros((200,200), np.uint8)
# cv2.rectangle(img,(0,100), (200,200),200,-1)

img = cv2.imread('me.jpg',0)

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()