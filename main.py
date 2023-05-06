import cv2
img = cv2.VideoCapture(0)
while True:
    ret, frame = img.read()
    cv2.imshow("PEGASUS", frame)
    if cv2.waitKey(1) == ord("q"):
        print("Quitted..")

        break
