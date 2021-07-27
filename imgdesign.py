import cv2
import numpy as np

img1 = cv2.imread('./img/parie.jpg')

print(len(img1),len(img1[0]))
roi = img1[25:355,300:440]
img1[25:25 + len(roi),450:450 + len(roi[0])] = roi
img1[25:25 + len(roi),300 - len(roi[0]):300] = roi
cv2.namedWindow('test')
cv2.imshow('test',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('./img/testcopy.jpg',img1)