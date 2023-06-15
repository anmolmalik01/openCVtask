# importing libraries
import cv2
import numpy as np

# video capture
cap = cv2.VideoCapture('video1.mp4')

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

count = 0

while True:
    ret, image = cap.read()

    #resizing image
    image = cv2.resize(image, (990, 540))

    # graying...
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detection object
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)

    # rectangle to the gate
    cv2.rectangle(image, (570, 0), (800, 500), (0, 0, 255), 2)

    # adding rectangle to the person
    for (x,y,w,h) in humans:
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)

    for (x,y,w,h) in humans:
        if(x>570 and x<800):
            if(y>0 and y<500):
                print("yaaa")
                # print(count)
                cv2.imwrite("frame%d.jpg" % count, image)
                count+=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

