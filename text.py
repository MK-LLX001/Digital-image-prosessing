
import cv2 ;
img = cv2.imread('./image/girl.jpg')

cv2.putText(img,"superman",(10,100),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),cv2.LINE_4)

cv2.imshow('Rectang',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
