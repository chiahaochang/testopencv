from typing import ClassVar

import cv2 as cv


img1 = cv.imread('./img/parie.jpg')
print(img1.shape)
print(len(img1),len(img1[0]))



roi1 = img1[150:300,600:700]
roi2 = img1[50:200,200:300]

dst = cv.addWeighted(roi1,0.7,roi2,0.3,0)
img1[50:200,200:300] = dst

cv.imshow('show',img1)
cv.waitKey(0)
cv.destroyAllWindows()