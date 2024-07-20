import cv2
import numpy as np

cap = cv2.VideoCapture("ball.mp4")
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (800, 600))
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            low = np.array([30, 70, 150])
            high = np.array([50, 255, 255])
            mask = cv2.inRange(frame_hsv, low, high)
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # finding contours
            cv2.drawContours(frame, contours, -1, (255, 0, 0), 2)  # drawing around contours
            cv2.imshow('result', frame)
            key = cv2.waitKey(1)
            if key == 115:
                cv2.waitKey(0)
            elif key == 113:
                print("video quited")
                break
        else:
            print("video finished")
            break
else:
    print("video not found")
