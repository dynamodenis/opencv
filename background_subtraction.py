import cv2

cap = cv2.VideoCapture('vid.mp4')
background = cv2.createBackgroundSubtractorMOG2(detectShadows=False
                                                
                                                )



while(cap.isOpened()):
    ret, frame = cap.read()
    
    if frame is None:
        break
    substractor = background.apply(frame)
    
        
    cv2.imshow('frame',substractor)
    # cv2.imshow('frame',frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()