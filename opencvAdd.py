from typing import ClassVar

import cv2 as cv

e1 = cv.getTickCount()
img1 = cv.imread('./img/light.jpg')
img2 = cv.imread('./img/opencvLogo.png')
print(img1.shape)
print(img2.shape)



roi1 = img1[0:377,0:427]
roi2 = img2[0:377,0:427]

dst = cv.addWeighted(roi1,0.5,roi2,0.5,0)
img1[0:377,0:427] = dst
cv.imshow('show',img1)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)
cv.waitKey(0)
cv.destroyAllWindows()