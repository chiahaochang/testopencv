import cv2


def drawcircle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img1,(x,y),10,(255,0,0),-1)


img1 = cv2.imread('./img/parie.jpg')
cv2.namedWindow('test',cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('test',drawcircle)
while(1):
    cv2.imshow('test',img1)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()