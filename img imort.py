import cv2                                   #first install (pip install opencv-python)
img = cv2.imread("panda.jpg",1)               # Then import cv2 and type this code
cv2.imshow("pic",img)
cv2.waitKey()
cv2.destroyAllWindows()
