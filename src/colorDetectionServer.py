#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy
from IEEE-OPEN.srv import *
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import time

def handle_detect_color(req):

    cam = cv2.VideoCapture(0)
    _, frame = cam.read()
    cam.release()
    return ColorDetectionResponse("Funcionou")

def colorDetectionServer():
    rospy.init_node('color_detection_server')
    s = rospy.Service('colorDetection', ColorDetection, handle_detect_color)
    print("Waiting to detect color")
    rospy.spin()

if __name__ == '__main__':
    try:
        colorDetectionServer()
    except rospy.ROSInterruptException: 
        pass
    
