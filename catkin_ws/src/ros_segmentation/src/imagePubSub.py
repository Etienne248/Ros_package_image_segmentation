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
    self.image_pub = rospy.Publisher("segMask",Image,queue_size=10)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    timestamp = data.header.stamp
    print(timestamp)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 300 :
      cv2.circle(cv_image, (300,150), 130, 0,-1)
      cv2.rectangle(cv_image, (300-200,200),(300+200,200+250), 0,-1)

    #cv2.imshow("pytorch_seg_receive", cv_image)
    #cv2.waitKey(3)

    msg = self.bridge.cv2_to_imgmsg(cv_image, "bgr8")
    msg.header.stamp = rospy.Time.now()
    try:
      self.image_pub.publish(msg)
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('pytorch_seg', anonymous=False)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)