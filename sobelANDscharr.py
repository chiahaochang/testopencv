import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/car.jpg', 0)

scharr = cv2.Scharr(img,cv2.CV_8U, 0, 1)
scharrx = cv2.Scharr(img,cv2.CV_8U, 1, 0)
scharry = cv2.Scharr(img,cv2.CV_8U, 0, 1)

plt.subplot(221), plt.imshow(scharr, cmap='gray'), plt.title('scharr')
plt.subplot(222), plt.imshow(scharrx, cmap='gray'), plt.title('scharr x')
plt.subplot(223), plt.imshow(scharry, cmap='gray'), plt.title('scharr y')

plt.show()