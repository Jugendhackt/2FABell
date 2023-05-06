#pip install opencv-python

import cv2                              #to import the package

img = cv2.VideoCapture(0)               #define the image
while True:
    ret, frame = img.read()             #read the image
    cv2.imshow("PEGASUS", frame)        #Here it appears in a window with title
    if cv2.waitKey(1) == ord("q"):      #To end Press q
        print("Quitted..")

        break
