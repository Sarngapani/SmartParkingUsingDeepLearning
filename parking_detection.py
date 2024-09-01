# parking_count_module.py

import cv2
import numpy as np
import pickle
import pandas as pd
from ultralytics import YOLO

def count_parking_slots(video_path, model_weights='yolov8s.pt', polyline_data='smparking1', class_file='coco.txt'):
    # Load polylines and area names
    with open(polyline_data, "rb") as f:
        data = pickle.load(f)
        polylines, areaNames = data['polylines'], data['areaNames']

    # Load class list
    with open(class_file, "r") as my_file:
        data = my_file.read()
        class_list = data.split("\n")

    # Load YOLO model
    model = YOLO(model_weights)

    cap = cv2.VideoCapture(video_path)

    filled_slots = []
    total_slots = len(polylines)

    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        count += 1
        if count % 3 != 0:
            continue

        frame = cv2.resize(frame, (1020, 500))
        frame_copy = frame.copy()
        results = model.predict(frame)
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")

        list1 = []
        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])

            c = class_list[d]
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            if 'car' in c:
                list1.append([cx, cy])

        filled_slots = []
        for i, polyline in enumerate(polylines):
            slot_filled = False
            for cx, cy in list1:
                result = cv2.pointPolygonTest(polyline, (cx, cy), False)
                if result >= 0:
                    slot_filled = True
                    break
            if slot_filled:
                filled_slots.append('red')  # Red for filled slots
            else:
                filled_slots.append('green')  # Green for empty slots

        print(filled_slots)
        carCount = len(list1)
        freeSpace = total_slots - carCount

        cap.release()
        cv2.destroyAllWindows()

        return total_slots, filled_slots, carCount, freeSpace
