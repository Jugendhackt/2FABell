#pip install opencv-python

import cv2

while True:
    capture = cv2.VideoCapture(0)

    cascade = cv2.CascadeClassifier("haarcascade_frontalface_from_github.xml")

    faces = ()

    while faces == ():
        camera = capture.read()
        print(camera)
        im_gray = cv2.cvtColor(camera[1], cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(im_gray)
        print("faces", faces)                       #Erkennt die Gesichter

        #print(camera[1].empty())

    for x, y, width, height in faces:
        cv2.rectangle(im_gray, (x,y), (x + width, y + height), color=(0,0, 255), thickness=5)

    cv2.imshow("PEGASUS", im_gray)
    cv2.waitKey(10000)

    capture.release()
    continue
    cv2.destroyAllWindows()
