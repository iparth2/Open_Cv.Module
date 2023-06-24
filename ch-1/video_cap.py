import cv2

cap = cv2.VideoCapture(r"C:\Users\Hp\Desktop\New folder\Assets\video_2023-04-22_09-45-18.mp4")

while True:
    success , img = cap.read()
    cv2.imshow("video screen" , img )

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break
