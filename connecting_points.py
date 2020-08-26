import cv2
import numpy as np

points=[]
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # This display the circles of the x and y coordinates in the window
        cv2.circle(img, (x,y), 5,(0,0,230),-1)
        points.append((x,y))
        
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(23,59,30),5)
            
        cv2.imshow('image',img)
        
    # this creates a dark image
img = np.zeros((512,512,3),np.uint8)

# this diaplay an image
# img = cv2.imread('comps.png')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
    
cv2.waitKey(0)
cv2.destroyAllWindows()