import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/car.jpg', 0)

scharr = cv2.Scharr(img,cv2.CV_8U, 0, 1)
scharrx = cv2.Scharr(img,cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(img,cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

plt.subplot(221), plt.imshow(scharr, cmap='gray'), plt.title('scharr')
plt.subplot(222), plt.imshow(scharrx, cmap='gray'), plt.title('scharr x')
plt.subplot(223), plt.imshow(scharry, cmap='gray'), plt.title('scharr y')
plt.subplot(224), plt.imshow(scharrxy, cmap='gray'), plt.title('Scharr XY')

plt.show()