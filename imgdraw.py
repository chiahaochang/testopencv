import cv2

img1 = cv2.imread('./img/parie.jpg')

print(len(img1), len(img1[0]))
cv2.line(img1,(200,100),(200,200),(0,0,255),10)
cv2.rectangle(img1,(100,50),(250,270),(0,255,0),10)
cv2.circle(img1,(300,250),50,(0,255,255),25)
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('./img/testcopy.jpg',img1)