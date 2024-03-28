import cv2


cap = cv2.VideoCapture("./image/Video.mp4")

while (cap.isOpened()):
    check, frame = cap.read()
    if check == True:
        cv2.imshow("video", frame)
        if cv2.waitKey(50) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows