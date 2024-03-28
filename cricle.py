import cv2 ;
img = cv2.imread('./image/gold.jpg')

cv2.circle(img,(750,500),(300),(255,255,10),5)

cv2.imshow('Rectang',img)
cv2.waitKey(0)
cv2.destroyAllWindows()