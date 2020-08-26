import cv2
import numpy as np

points=[]
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # This display the circles of the x and y coordinates in the window
        blue=[x,y,0]
        green=[x,y,1]
        red=[x,y,2]
        cv2.circle(img,(x,y), 3, (0,0,200), -1)
        newimage=np.zeros((512,512,3), np.uint8)
        
        newimage[:]=[blue,green,red]
        cv2.imshow('image',newimage)
        
    # this creates a dark image
img = np.zeros((512,512,3),np.uint8)

# this diaplay an image
# img = cv2.imread('comps.png')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
    
cv2.waitKey(0)
cv2.destroyAllWindows()