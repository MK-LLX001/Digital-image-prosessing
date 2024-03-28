# FIXME: Show image in image  

import cv2 
img = cv2.imread('./image/color.jpg')

# TODO: arrowLine (image , that star , end and color (RGB color)) 

cv2.arrowedLine(img,(20,20),(360,200),(255,0.0),5)
cv2.arrowedLine(img,(20,20),(200,400),(255,0.0),5)
cv2.arrowedLine(img,(20,20),(550,550),(255,210.0),5)
cv2.imshow('Arrow Line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

