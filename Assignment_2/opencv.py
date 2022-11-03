#open camera and display video
import cv2

cap = cv2.VideoCapture(0)
#while camera is opened, write frames to video file
while True:
    if cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Camera not opened")
        
cap.release()
cv2.destroyAllWindows()