import cv2

cap = cv2.VideoCapture(0)

cap.set(3,140)
cap.set(4,280)

while True:
    success , img = cap.read()
    cv2.imshow("video screen" , img )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
