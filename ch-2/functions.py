import cv2

img = cv2.imread(r"C:\Users\Hp\Desktop\New folder\Assets\wp\thumb-1920-949023.jpg")

img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img, (17,7),0)

cv2.imshow("Gray img" , img_gray)
cv2.imshow("blur img" , img_blur)

cv2.waitKey(0)