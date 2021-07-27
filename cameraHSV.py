import cv2
import numpy as np

def nothing(x):
    pass

#開圖

cv2.namedWindow('frame')
cv2.createTrackbar('A','frame',0,255,nothing)
cv2.createTrackbar('B','frame',0,255,nothing)
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    A = cv2.getTrackbarPos('A','frame')
    B = cv2.getTrackbarPos('B','frame')
    lower_blue = np.array([A,50,50])
    upper_blue = np.array([B,255,255])
    
    mask = cv2.inRange(frame2, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame,frame, mask = mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('img2',frame2)
    cv2.imshow('res',res)
    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()