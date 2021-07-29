import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./img/light.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
mask[250:800,500:1500] = 255
mask_img = cv2.bitwise_and(img,img,mask = mask)

hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(321), plt.imshow(img),plt.title('Image1')
plt.subplot(322), plt.plot(hist_full), plt.title('Image1 title'),plt.xlim([0,256])
plt.subplot(323), plt.imshow(mask_img, 'gray'),plt.title('masked_image')
plt.subplot(324), plt.plot(hist_mask), plt.title('masked_image title'),plt.xlim([0,256])
plt.subplot(325), plt.imshow(mask, 'gray'),plt.title('mask value')
plt.subplot(326), plt.plot(hist_full), plt.plot(hist_mask), plt.title('all'), plt.xlim([0,256])
plt.show()