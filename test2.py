import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/parie.jpg')
cv2.imshow('paries', img)
cv2.waitKey(0)
cv2.destroyAllWindows()