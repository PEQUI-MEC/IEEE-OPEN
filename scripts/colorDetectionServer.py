#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy
import sys
from openpkg.srv import *
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import time

def handle_detect_color(req):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imshow("Original", frame)
    time.sleep(2)
    cam.release()
    cv2.destroyAllWindows()
    return ColorDetectionResponse("Funcionou")

def colorDetectionServer():
    rospy.init_node('colorDetectionserver')
    s = rospy.Service('colorDetectionserver', ColorDetection, handle_detect_color)
    print("Waiting to detect color")
    rospy.spin()

if __name__ == '__main__':
    try:
        colorDetectionServer()
    except rospy.ROSInterruptException:
        pass
    
