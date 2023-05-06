#pip install opencv-python

import cv2

img = cv2.VideoCapture(0)               #deffinge the image
while True:
    ret, frame = img.read()             #read the image
    cv2.imshow("PEGASUS", frame)        #Here it shows
    if cv2.waitKey(1) == ord("q"):      #To end Press q
        print("Quitted..")

        break
