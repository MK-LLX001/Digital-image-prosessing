
import cv2;
import datetime ; 
cap = cv2.VideoCapture(0) # ดืงข้อมูนvideo มาจาก ก้อง 

while (cap.isOpened()):  #กวดสอบว่า ก้องไดเปีดแล้วหรือ บ่อ
    check, frame = cap.read()
    if check == True:
        currentDate = str(datetime.datetime.now())
        # cv2.putText(frame, currentDate(50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.putText(frame,currentDate,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        
        cv2.imshow("video", frame)
        if cv2.waitKey(50) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllwindows()