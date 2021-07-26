import cv2

img1 = cv2.imread('./img/rem.png')
cv2.imshow('rem',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()