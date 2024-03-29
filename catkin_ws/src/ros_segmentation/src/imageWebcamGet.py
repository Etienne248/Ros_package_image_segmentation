#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
cap = cv2.VideoCapture(0) 
print(cap.isOpened())
bridge = CvBridge()
def talker():
  pub = rospy. Publisher('image', Image, queue_size = 10) 
  rospy.init_node("camera", anonymous = False) 
  rate = rospy.Rate(10)
  while not rospy.is_shutdown(): 
    ret, frame = cap.read()
    if not ret:
      break

    msg = bridge.cv2_to_imgmsg(frame, "bgr8") 
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = 'camera_frame'
    pub.publish(msg)

    cv2.imshow('camera image Window',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    
  cap.release()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass