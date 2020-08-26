import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # This display the text of the x and y coordinates in the window
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x) + " , " + str(y)
        cv2.putText(img,strXY,(x,y),font,1,(200,200,200),2)
        cv2.imshow('image',img)
        
        # Listen to a rght button click
    if event == cv2.EVENT_RBUTTONDOWN:
        # finds cordinates of blue color
        blue=img[y,x,0]
        # finds cordinates of green color
        green=img[y,x,1]
        # finds cordinates of red color
        red=img[y,x,2]
        
        # display the color cordinates
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR=str(blue) + " , " + str(green) + "," + str(red)
        cv2.putText(img,strBGR,(x,y),font,0.5,(200,200,200),2)
        cv2.imshow('image',img)

    # this creates a dark image
# img = np.zeros((512,512,3),np.uint8)

# this diaplay an image
img = cv2.imread('comps.png')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
    
cv2.waitKey(0)
cv2.destroyAllWindows()