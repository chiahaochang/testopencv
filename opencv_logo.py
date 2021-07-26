import cv2

img1 = cv2.imread('./img/whit.jpg')
#print(len(img1),len(img1[0]))
cv2.rectangle(img1,(0,0),(225,225),(0,0,255),10)
cv2.circle(img1,(114,50),30,(255,0,0),15)
cv2.imshow('opencv',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("img/opencv.jpg",img1)