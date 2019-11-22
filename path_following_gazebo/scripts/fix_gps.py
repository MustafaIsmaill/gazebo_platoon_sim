#!/usr/bin/env python
import tf
import rospy
from nav_msgs.msg import Odometry

def callback(data):
    data.header.frame_id = "world"
    data.child_frame_id = FRAME_ID

    roll, pitch, yaw = tf.transformations.euler_from_quaternion([data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w])
    new_or = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
    data.pose.pose.orientation.x = new_or[0]
    data.pose.pose.orientation.y = new_or[1]
    data.pose.pose.orientation.z = new_or[2]
    data.pose.pose.orientation.w = new_or[3]

    trans = [data.pose.pose.position.x, data.pose.pose.position.y, 0.0]

    br.sendTransform(trans, new_or, rospy.Time.now(), FRAME_ID, "world")
    pub.publish(data)
    
def listener():

    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("perfect_gps/utm", Odometry, callback)

    rospy.spin()

if __name__ == '__main__':
    FRAME_ID = ""
    ns = rospy.get_namespace()
    if(ns == "/fusion1/"):
        FRAME_ID = "fs1/base_footprint"
    elif(ns == "/fusion2/"):
        FRAME_ID = "fs2/base_footprint"
    elif(ns == "/fusion3/"):
        FRAME_ID = "fs3/base_footprint"

    br = tf.TransformBroadcaster()
    pub = rospy.Publisher("perfect_gps/utm_fixed", Odometry, queue_size=10)
    listener()