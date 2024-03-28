import cv2

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    check, frame = cap.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllwindows()
