import pickle

import cv2
import cvzone
import numpy as np
import cvzone

cap = cv2.VideoCapture("easy.mp4")

drawing=False
areaNames=[]
try:
    with open("smparking1", "rb") as f:
        data=pickle.load(f)
        polylines,areaNames=data['polylines'],data['areaNames']
except:
    polylines = []
points=[]
currentName=" "
def draw(event,x,y,flags,param):
    global points,drawing
    drawing=True
    if event==cv2.EVENT_LBUTTONDOWN:
        points=[(x,y)]
    elif event== cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x,y))
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        currentName=input("Area Name: ")
        if currentName:
            areaNames.append(currentName)
            polylines.append(np.array(points,np.int32))

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    frame=cv2.resize(frame,(1020,500))
    for i,polyline in enumerate (polylines):
        print(i)
        cv2.polylines(frame,[polyline],True,(0,0,255),2)
        cvzone.putTextRect(frame,f'{areaNames[i]}',tuple(polyline[0]),1,1)
    cv2.imshow('FRAME', frame)
    cv2.setMouseCallback('FRAME',draw)
    Key = cv2.waitKey(1) & 0xFF
    if Key== ord('s'):
        with open("smparking1","wb") as f:
            data={'polylines':polylines,'areaNames':areaNames}
            pickle.dump(data,f)

cap.release()
cv2.destroyAllWindows()
