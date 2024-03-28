# import cv2 ;

# img = cv2.imread('./image/gold.jpg')

# cv2.rectangle(img,(500,300),(1020,710),(255,255,10),4)
# cv2.imshow('Rectang',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#  TODO: this is work shop 


import cv2 ;

img = cv2.imread('./image/box_color.jpg')

cv2.rectangle(img,(5,195),(195,5),(255,255,10),-1)
cv2.rectangle(img,(195,193),(391,3),(255,25,10),-1)
# TODO:  right 
cv2.rectangle(img,(5,195),(195,391),(255,210,70),-1)
cv2.rectangle(img,(195,195),(391,391),(255,230,210),-1)
# cv2.rectangle(img,(195,193),(391,3),(255,25,10),4)
cv2.imshow('Rectang',img)
cv2.waitKey(0)
cv2.destroyAllWindows()