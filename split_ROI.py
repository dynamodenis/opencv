import cv2
import numpy as np



# this diaplay an image
img = cv2.imread('comps.png')
img2 = cv2.imread('me.jpg')


b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# ROI crops image to another part
laptop = img[400:400, 400:400]
img[300:300, 300:300] = laptop

# resize the image to the same  resolution to merge them
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# Add two images together
# join = cv2.add(img,img2)

# This merges the 2 imges and increases th opacity of one image over the other
join = cv2.addWeighted(img,.9,img2,.1,0)
cv2.imshow('image',join)

    
cv2.waitKey(0)
cv2.destroyAllWindows()