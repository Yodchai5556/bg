# For more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import cv2
import time
import numpy as np
def times(s_time,e_time):
    i=0
    if(s_time>=56):
        e_time=e_time+(61-s_time);
        s_time=0
    while(s_time<e_time):
        
        i=i+1
        s_time=s_time+1
    return i
# Playing video from file:
# cap = cv2.VideoCapture('vtest.avi')
# Capturing video from webcam:
cap = cv2.VideoCapture(0)
s_time=int(time.strftime('%S'))
e_time=int(time.strftime('%S'))
currentFrame = 0
while(times(s_time,e_time)<10):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Handles the mirroring of the current frame
    frame = cv2.flip(frame,1)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB )

    # Saves image of the current frame in jpg file
    # name = 'frame' + str(currentFrame) + '.jpg'
    cv2.imwrite("eiei.jpg", frame)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # To stop duplicate images
    e_time=int(time.strftime('%S'))
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()