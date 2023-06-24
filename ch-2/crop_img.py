import cv2
img = cv2.imread(r"C:\Users\Hp\Desktop\New folder\Assets\wp\wallpaperflare.com_wallpaper (1).jpg")
img = cv2.resize(img,(920,580))


cropped_img = img[0:300 , 200:600]  #here we dont use cv functions instead of it we use matrix, where height came first than follows width


cv2.imshow("img" , img)
cv2.imshow("cropped.img" , cropped_img)
cv2.waitKey(0)