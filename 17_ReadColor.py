import cv2;

img = cv2.imread('./image/color_ciecles.jpg')
def clickPosition(event, x, y , Flags, params):
     if event == cv2.EVENT_LBUTTONDOWN: #ส้างปุ่มกดแล้วให้สะแดงค่า
        blue = img[y,x,0] # set color blue 
        green = img[y,x,1] # set color green
        red = img[y,x,2] # set color red
        text = str(blue)+"-"+str(green)+"-"+str(red) #displayText color and use - between
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_4) # set position img and set font size 
        cv2.imshow('output',img)
cv2.imshow('output',img)
cv2.setMouseCallback("output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()