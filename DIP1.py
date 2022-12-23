# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
img_path="C:/Users/Asus/OneDrive/Desktop/DIP Workshop/sherlock_kid.png"
img=cv2.imread(img_path)
print(img)
#cv2.imshow("Image",img)
#cv2.waitKey(1000000)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image",img_gray)
#cv2.waitKey(0)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV Image",img_hsv)

cv2.imwrite("C:/Users/Asus/OneDrive/Desktop/DIP Workshop/sherlock_kid_gray.png",img_gray)

print(img.shape)
print(img_gray.shape)
img_resized=cv2.resize(img,(100,100))
#cv2.imshow("Resized Image",img_resized)
img_crop=img_resized[0:250,300:760]
cv2.imshow("Cropped image",img_crop)
cv2.waitKey(10000)



