#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np

global blue_min; global blue_max
global green_min; global green_max
global red_min; global red_max

global BLUE; BLUE = 'Blue Calibration'
global GREEN; GREEN = 'Green Calibration'
global RED; RED = 'Red Calibration'
cam = cv2.VideoCapture(0)

def callback(value):
    pass

def createBlueTrackbar():
    cv2.namedWindow("Blue Calibration")
    cv2.createTrackbar('H_min', 'Blue Calibration', 0, 360, callback)
    cv2.createTrackbar('S_min', 'Blue Calibration', 0, 100, callback)
    cv2.createTrackbar('V_min', 'Blue Calibration', 0, 100, callback)

    cv2.createTrackbar('H_max', 'Blue Calibration', 0, 360, callback)
    cv2.createTrackbar('S_max', 'Blue Calibration', 0, 100, callback)
    cv2.createTrackbar('V_max', 'Blue Calibration', 0, 100, callback)

def createGreenTrackbar():
    cv2.namedWindow("Green Calibration")
    cv2.createTrackbar('H_min', 'Green Calibration', 0, 360, callback)
    cv2.createTrackbar('S_min', 'Green Calibration', 0, 100, callback)
    cv2.createTrackbar('V_min', 'Green Calibration', 0, 100, callback)

    cv2.createTrackbar('H_max', 'Green Calibration', 0, 360, callback)
    cv2.createTrackbar('S_max', 'Green Calibration', 0, 100, callback)
    cv2.createTrackbar('V_max', 'Green Calibration', 0, 100, callback)

def createRedTrackbar():
    cv2.namedWindow("Red Calibration")
    cv2.createTrackbar('H_min', 'Red Calibration', 0, 360, callback)
    cv2.createTrackbar('S_min', 'Red Calibration', 0, 100, callback)
    cv2.createTrackbar('V_min', 'Red Calibration', 0, 100, callback)

    cv2.createTrackbar('H_max', 'Red Calibration', 0, 360, callback)
    cv2.createTrackbar('S_max', 'Red Calibration', 0, 100, callback)
    cv2.createTrackbar('V_max', 'Red Calibration', 0, 100, callback)

def screenCalibration(colorName):
    global blue_min; global blue_max
    global green_min; global green_max
    global red_min; global red_max

    if colorName is BLUE:

        createBlueTrackbar()

        while True:
            _, frame = cam.read()
            frame = cv2.flip(frame,1)#BGR
            frame = cv2.blur(frame, (5,5),0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            hBlue_min = np.interp(cv2.getTrackbarPos('H_min', 'Blue Calibration'), [0,360],[0,179])
            sBlue_min = np.interp(cv2.getTrackbarPos('S_min', 'Blue Calibration'), [0,100],[0,255])
            vBlue_min = np.interp(cv2.getTrackbarPos('V_min', 'Blue Calibration'), [0,100],[0,255])

            hBlue_max = np.interp(cv2.getTrackbarPos('H_max', 'Blue Calibration'), [0,360],[0,179])
            sBlue_max = np.interp(cv2.getTrackbarPos('S_max', 'Blue Calibration'), [0,100],[0,255])
            vBlue_max = np.interp(cv2.getTrackbarPos('V_max', 'Blue Calibration'), [0,100],[0,255])

            blue_min = np.array([hBlue_min,sBlue_min,vBlue_min])
            blue_max = np.array([hBlue_max,sBlue_max,vBlue_max])

            mask = cv2.inRange(hsv, blue_min, blue_max)

            results = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow(BLUE, results)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # cv2.destroyAllWindows()
                cv2.destroyWindow(BLUE)
                break
                
    elif colorName is GREEN:

        createGreenTrackbar()

        while True:
            _, frame = cam.read()
            frame = cv2.flip(frame,1)#BGR
            frame = cv2.blur(frame, (5,5),0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            hGreen_min = np.interp(cv2.getTrackbarPos('H_min', 'Green Calibration'), [0,360],[0,179])
            sGreen_min = np.interp(cv2.getTrackbarPos('S_min', 'Green Calibration'), [0,100],[0,255])
            vGreen_min = np.interp(cv2.getTrackbarPos('V_min', 'Green Calibration'), [0,100],[0,255])

            hGreen_max = np.interp(cv2.getTrackbarPos('H_max', 'Green Calibration'), [0,360],[0,179])
            sGreen_max = np.interp(cv2.getTrackbarPos('S_max', 'Green Calibration'), [0,100],[0,255])
            vGreen_max = np.interp(cv2.getTrackbarPos('V_max', 'Green Calibration'), [0,100],[0,255])

            green_min = np.array([hGreen_min,sGreen_min,vGreen_min])
            green_max = np.array([hGreen_max,sGreen_max,vGreen_max])

            mask = cv2.inRange(hsv, green_min, green_max)

            results = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow(GREEN, results)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # cv2.destroyAllWindows()
                cv2.destroyWindow(GREEN)
                break
            
    elif colorName is RED:

        createRedTrackbar()

        while True:
            _, frame = cam.read()
            frame = cv2.flip(frame,1)#BGR
            frame = cv2.blur(frame, (5,5),0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            hRed_min = np.interp(cv2.getTrackbarPos('H_min', 'Red Calibration'), [0,360],[0,179])
            sRed_min = np.interp(cv2.getTrackbarPos('S_min', 'Red Calibration'), [0,100],[0,255])
            vRed_min = np.interp(cv2.getTrackbarPos('V_min', 'Red Calibration'), [0,100],[0,255])

            hRed_max = np.interp(cv2.getTrackbarPos('H_max', 'Red Calibration'), [0,360],[0,179])
            sRed_max = np.interp(cv2.getTrackbarPos('S_max', 'Red Calibration'), [0,100],[0,255])
            vRed_max = np.interp(cv2.getTrackbarPos('V_max', 'Red Calibration'), [0,100],[0,255])

            red_min = np.array([hRed_min,sRed_min,vRed_min])
            red_max = np.array([hRed_max,sRed_max,vRed_max])

            mask = cv2.inRange(hsv, red_min, red_max)

            results = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow(RED, results)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # cv2.destroyAllWindows()
                cv2.destroyWindow(RED)
                break

    cv2.destroyAllWindows()

def saveValues():
    arq = open('/home/open/catkin_ws/src/calibrationColors', 'w')
    text = []
    for i in range(0,3):
        if i is 0:
            text.append('BLUE_MIN\t')
            for x in blue_min:
                text.append(str(x))
                text.append('\t')
            text.append('\n')

            text.append('BLUE_MAX\t')
            for x in blue_max:
                text.append(str(x))
                text.append('\t')
            text.append('\n')

        elif i is 1:
            text.append('GREEN_MIN\t')
            for x in green_min:
                text.append(str(x))
                text.append('\t')
            text.append('\n')

            text.append('GREEN_MAX\t')
            for x in green_max:
                text.append(str(x))
                text.append('\t')
            text.append('\n')

        elif i is 2:
            text.append('RED_MIN\t')
            for x in red_min:
                text.append(str(x))
                text.append('\t')
            text.append('\n')

            text.append('RED_MAX\t')
            for x in red_max:
                text.append(str(x))
                text.append('\t')
            text.append('\n')
    
    arq.writelines(text)
    arq.close()

if __name__ == '__main__':
    screenCalibration(BLUE)
    screenCalibration(GREEN)
    screenCalibration(RED)
    saveValues()