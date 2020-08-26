import cv2
import datetime

cap = cv2.VideoCapture(0)
# when u want u save the video follow below
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save = cv2.VideoWriter('webcam.avi', fourcc,20.0,(640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
    
    # check iif the frame is true then write the video
    if ret:
        # in set the font
        
        font = cv2.FONT_HERSHEY_COMPLEX
        date = str(datetime.datetime.now())
        text = 'Weight' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "Height" + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        frame = cv2.putText(frame, date, (10,50), font, 1, (0,34,200), 1, cv2.LINE_AA)
        
        cv2.imshow('frame',frame)
        # cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else:
        break
    
cap.release()
cv2.destroyAllWindows()