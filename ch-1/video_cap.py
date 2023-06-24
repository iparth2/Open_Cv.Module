import cv2

cap = cv2.VideoCapture(r"C:\Users\Hp\Desktop\cv\assets\video_2023-04-29_22-29-11.mp4")

while True:
    success , img = cap.read()
    cv2.imshow("video screen" , img )

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break
