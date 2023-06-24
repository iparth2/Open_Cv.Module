import cv2

img = cv2.imread(r"C:\Users\Hp\Desktop\New folder\Assets\wp\wp8402317.jpg")


print(img.shape) # GIVES THE DIMENSIONS OF THE IMG 


img_1 = cv2.resize(img ,(640,480)) #resizing the img 


#cv2.imshow("img",img)
cv2.imshow("img_1",img_1)

cv2.waitKey(0)

