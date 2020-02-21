import cv2
img = cv2.imread("panda.jpg",1)
cv2.imshow("pic",img)
cv2.waitKey()
cv2.destroyAllWindows()