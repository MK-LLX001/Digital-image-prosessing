import cv2 ;
img = cv2.imread('./image/box_color.jpg')

cv2.circle(img,(97,97),(30),(255,255,10),5)
cv2.circle(img,(297,97),(30),(0,255,10),5)

cv2.circle(img,(97,297),(30),(0,25,10),5)
cv2.circle(img,(297,297),(30),(255,55,10),5)
cv2.imshow('Rectang',img)
cv2.waitKey(0)
cv2.destroyAllWindows()