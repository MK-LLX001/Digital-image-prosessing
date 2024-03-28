import cv2;

img = cv2.imread('./image/Coin.jpg')
def clickPosition(event, x, y , Flags, params):
     if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),cv2.LINE_4)
        cv2.imshow('output',img)
cv2.imshow('output',img)
cv2.setMouseCallback("output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()