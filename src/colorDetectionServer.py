#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy
from ieee_open.srv import *
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import time
import numpy as np

# global blue_min; blue_min = [];      global blue_max; blue_max = []
# global green_min; green_min = [];    global green_max; green_max = []
# global red_min; red_min = [];        global red_max; red_max = []
global blue_min;    global blue_max
global green_min;   global green_max
global red_min;     global red_max

def loadValues():
    global blue_min;    global blue_max
    global green_min;   global green_max
    global red_min;     global red_max

    try:
        arq = open('/home/open/catkin_ws/src/calibrationColors.txt', 'r')
        text = arq.readlines()
        
        for line in text:
            content = []
            content = line.split()
            
            if content[0] == 'BLUE_MIN':
                # for i in range (1,len(content)):
                #     blue_min.append(float(content[i]))
                blue_min = np.array([content[1], content[2], content[3]])
                print(blue_min)

            elif content[0] == 'BLUE_MAX':
                # for i in range (1,len(content)):
                #     blue_max.append(float(content[i]))
                blue_max = np.array([content[1], content[2], content[3]])

            elif content[0] == 'GREEN_MIN':
                # for i in range (1,len(content)):
                #     green_min.append(float(content[i]))
                green_min = np.array([content[1], content[2], content[3]])

            elif content[0] == 'GREEN_MAX':
                # for i in range (1,len(content)):
                #     green_max.append(float(content[i]))
                green_max = np.array([content[1], content[2], content[3]])
            
            elif content[0] == 'RED_MIN':
                # for i in range (1,len(content)):
                #     red_min.append(float(content[i]))
                red_min = np.array([content[1], content[2], content[3]])

            elif content[0] == 'RED_MAX':
                # for i in range (1,len(content)):
                #     red_max.append(float(content[i]))
                red_max = np.array([content[1], content[2], content[3]])

        arq.close()
    except IOError:
        print("The File could not be openned!")
        sys.exit()

def handle_detect_color(req):
    # global blue_min;    global blue_max
    # global green_min;   global green_max
    # global red_min;     global red_max

    cam = cv2.VideoCapture(0)

    _, frame = cam.read() #BGR
    frame = cv2.flip(frame,1)   #BGR
    frame = cv2.blur(frame, (5,5),0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #HSV
    print(blue_min)

    mask_blue = cv2.inRange(hsv, blue_min, blue_max)
    mask_green = cv2.inRange(hsv, green_min, green_max)
    mask_red = cv2.inRange(hsv, red_min, red_max)


    _, contornosBlue, hierarchyBlue = cv2.findContours(mask_blue.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, contornosGreen, hierarchyGreen = cv2.findContours(mask_green.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, contornosRed, hierarchyRed = cv2.findContours(mask_red.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornosBlue) > 0:

        maior_contorno = max(contornosBlue,    key=cv2.contourArea)
        # segundo_maior_contorno = max(contornos-maior_contorno, key=cv2.contourArea)

        cv2.drawContours(resultados, maior_contorno, -1, (255,0,0), 3)
        ((x, y), raio) = cv2.minEnclosingCircle(maior_contorno)
        # cv2.circle(resultados, (int(x), int(y)), int(raio),(0, 255, 255), 2)

        M = cv2.moments(maior_contorno)

        if M['m00'] > 0 and M['m00'] > 0:
            centroide = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        if raio > 10:
            # cv2.circle(frame, (int(x), int(y)), int(raio),(0, 255, 255), 2)
            cv2.circle(frame, centroide, 3, (0, 0, 255), -1)
            cv2.putText(frame,"Centroide", (centroide[0]+10,centroide[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
            cv2.putText(frame,"("+str(centroide[0])+","+str(centroide[1])+")", (centroide[0]+10,centroide[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
            
            cor_hsv = hsv[centroide[1], centroide[0]]

            cv2.putText(frame,"("+str(cor_hsv[0])+","+str(cor_hsv[1])+")"+str(cor_hsv[2]), (centroide[0]+30,centroide[1]+35), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
    else:
        print("Blue containner couldn't be founded")
    
    cv2.imshow("Resultados", frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return ColorDetectionResponse("Funcionou")

def colorDetectionServer():
    rospy.init_node('color_detection_server')
    s = rospy.Service('colorDetection', ColorDetection, handle_detect_color)
    print("Waiting to detect color")
    rospy.spin()

if __name__ == '__main__':
    try:
        loadValues()
        colorDetectionServer()
    except rospy.ROSInterruptException: 
        pass