import numpy as np
import cv2
import random
import time

def videocap():

    cap = cv2.VideoCapture(1)
    i=0

    while(True):
    # Capture frame-by-frame
        ret, frame = cap.read()
    
    #time.sleep(10)
        if(i%6000==0):
            cv2.imwrite('images/{index}.jpg'.format(index=int(i/6000)),frame)
        i+=1
    
        cv2.imshow('frame',frame)
    #time.sleep(10)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

