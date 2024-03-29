#!/usr/bin/env python3
from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    
    self.image_sub = rospy.Subscriber("image",Image,self.callback2)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("segMask",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    timestamp = data.header.stamp
    print(timestamp)

    cv2.imshow("mask Image window", cv_image)
    cv2.waitKey(3)

  def callback2(self,data):
    pass

def main(args):
  ic = image_converter()
  rospy.init_node('mask_processing', anonymous=False)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)