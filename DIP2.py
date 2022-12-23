# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
import numpy as np
#img_path="C:/Users/Asus/OneDrive/Desktop/DIP_ Workshop/sherlock_kid.png"
#img=cv2.imread(img_path)
#white_img=np.full(img.shape,255,dtype=np.uint8)#converts into unsigned integer of 8 bit
#white_img=np.copy(img)
#white_img[:,:,:]=255
#neg_img=white_img-img
#cv2.imshow("Image",white_img)
#cv2.waitKey(0)
#add img+red_img(0,0,50) and see the output
#red_img=np.copy(img)
#red_img[:,:]=[0,0,50]
#cv2.imshow("Image",red_img+img)
#cv2.waitKey(0)

#img_path="C:/Users/Asus/OneDrive/Desktop/DIP_ Workshop/book_page.jpg"
#img=cv2.imread(img_path)

#gray_scale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#thresh_val,thresh_img=cv2.threshold(gray_scale_img,90,89,cv2.THRESH_OTSU)
#cv2.imshow("Original Image",img)
#print(thresh_val)


#(h, w) = gray_scale_img.shape
#for x in range(0,h):
 #   for y in range(0,w):
  #      #print(gray_scale_img[x,y])
   #     if gray_scale_img[x,y]>127:
    #        gray_scale_img[x,y]=255
     #   else:
      #      gray_scale_img[x,y]=0

#cv2.imshow("converted image",gray_scale_img)
#cv2.waitKey(0)



def nothing(x):
    pass

def createTrackbar():
    cv2.namedWindow("thresholding")
    #cv2.namedWindow("thresholding1")
    cv2.createTrackbar("H_min","thresholding",0,255,nothing)
    cv2.createTrackbar("S_min", "thresholding", 0, 255, nothing)
    cv2.createTrackbar("V_min", "thresholding", 0, 255, nothing)
    cv2.createTrackbar("H_max", "thresholding", 0, 255, nothing)
    cv2.createTrackbar("S_max", "thresholding", 0, 255, nothing)
    cv2.createTrackbar("V_max", "thresholding", 0, 255, nothing)
    #cv2.createTrackbar("track","thresholding1",0,255,nothing)


img_path="C:/Users/Asus/OneDrive/Desktop/DIP_ Workshop/hand.jpg"
img = cv2.imread(img_path)
#cv2.imshow("Original image",img)
gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray scale image",gray_scale)
_,thresh_img=cv2.threshold(gray_scale,127,255,cv2.THRESH_BINARY)
#cv2.imshow("thres",thresh_img)

createTrackbar()
while True:
    H_min=cv2.getTrackbarPos("H_min","thresholding")
    S_min=cv2.getTrackbarPos("S_min","thresholding")
    V_min=cv2.getTrackbarPos("V_min","thresholding")
    H_max=cv2.getTrackbarPos("H_max","thresholding")
    S_max=cv2.getTrackbarPos("S_max","thresholding")
    V_max=cv2.getTrackbarPos("V_max","thresholding")
    #track=cv2.getTrackbarPos("track","thresholding1")
    #print(track)
    #print(T)
    #_,thresh_img=cv2.threshold(gray_scale,T,255,cv2.THRESH_BINARY)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([H_min,S_min,V_min])
    upper=np.array([H_max,S_max,V_max])

    thresh_img=cv2.inRange(img_hsv,lower,upper)
    cv2.imshow("img",thresh_img)
    imgCopy=img.copy()
    contours,_=cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#returns list of contours
    #print(contours)
    cv2.drawContours(imgCopy,contours,-1,(255,0,0),2)#-1 draws all contours
    cv2.imshow("image",imgCopy)
    key=cv2.waitKey(1000)
    if(key==ord('q')):
        break
#print(T)
#cv2.destroyAllWindows()


