# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
video_reader=cv2.VideoCapture(0) #read input from webcam
while True:
    success,frame=video_reader.read()
    if not success:
        break

    cv2.imshow("My Video",frame)
    key=cv2.waitKey(10) #gives time to show a frame
    if key==ord('q'):
        break

video_reader.release()
cv2.destroyAllWindows()



