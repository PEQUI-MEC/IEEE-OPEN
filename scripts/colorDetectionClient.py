#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy
from ieee_open.srv import *
# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

def colorDetectionClient():
    rospy.wait_for_service('colorDetection')
    try:
        color_detection = rospy.ServiceProxy('colorDetection', ColorDetection)
        resp1  = color_detection('Teste')
        print(resp1.founded)
    # except (rospy.ServiceException, e):
    #     print ("Service call failed: %s"%e)
    except (rospy.ServiceException):
        print ("Service call failed")


if __name__ == '__main__':
    colorDetectionClient()