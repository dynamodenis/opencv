import cv2

cap = cv2.VideoCapture(0)
# when u want u save the video follow below
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save = cv2.VideoWriter('webcam.avi', fourcc,20.0,(640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
    
    # check iif the frame is true then write the video
    if ret:
        save.write(frame)
        
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
    
        # optional if u want to convert it to grey
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # in the imshow method change frame to gray
        
        cv2.imshow('frame',gray)
        # cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else:
        break
    
cap.release()
cap.release()
cv2.destroyAllWindows()