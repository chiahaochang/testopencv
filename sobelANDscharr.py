import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/car.jpg', 0)

sobel = cv2.Sobel(img,cv2.CV_16U, 1, 1, ksize = 1)
sobel5 = cv2.Sobel(img,cv2.CV_16U, 1, 1,ksize= 5)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize = 5)

plt.subplot(221), plt.imshow(sobelx, cmap='gray'), plt.title('sobelx')
plt.subplot(222), plt.imshow(sobely, cmap='gray'), plt.title('sobely')
plt.subplot(223), plt.imshow(sobel, cmap='gray'), plt.title('ksize 3')
plt.subplot(224), plt.imshow(sobel, cmap='gray'), plt.title('ksize 5')

plt.show()