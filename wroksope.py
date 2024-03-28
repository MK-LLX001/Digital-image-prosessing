import cv2 ;
img = cv2.imread('./image/Coin.jpg')
#ตำแหนง มขะหนาด สี
cv2.circle(img,(345,83),(65),(255,255,10),5)
cv2.circle(img,(172,183),(70),(255,255,10),5)
cv2.circle(img,(414,245),(60),(255,255,10),5)
cv2.circle(img,(590,139),(85),(255,255,10),5)
cv2.circle(img,(90,382),(78),(255,255,10),5)
cv2.circle(img,(318,384),(70),(255,255,10),5)
cv2.circle(img,(526,423),(80),(255,255,10),5)
cv2.circle(img,(652,344),(60),(255,255,10),5)

cv2.imshow('Rectang',img)
cv2.waitKey(0)
cv2.destroyAllWindows()