#!/usr/bin/env python3

from os import system
import rospy
import tf
from apriltag_ros.msg import AprilTagDetectionArray

def callback(data):

    
    for i in range(len(data.detections)):
        #print(len(data.detections))
        #print(data.detections[i].id[0])
        #print(data.detections[i].pose.pose.pose)
        tag_name = "/tag_" + str(data.detections[i].id[0])
        (trans, quat) = listener.lookupTransform(tag_name, "/map", rospy.Time(0))
        #apriltags[data.detections[i].id[0]] = data.detections[i].pose.pose.pose
        apriltags[data.detections[i].id[0]] = (trans, quat)

if __name__ == '__main__':
    rospy.init_node('Node', anonymous=True)
    listener = tf.TransformListener()
    apriltags = {}
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        #print("abc")
        sub = rospy.Subscriber("/tag_detections", AprilTagDetectionArray, callback)
        rate.sleep()
    
    with open("apriltags_location.txt", 'w') as f: 
        for key, value in apriltags.items(): 
            f.write('%s:%s\n' % (key, value))
    
    system("clear")
    print("Final Data:\n")
    print(apriltags)
