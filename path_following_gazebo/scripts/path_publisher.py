#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

# ns = rospy.get_namespace()
# ns = ns[1:]

def make_path():
    file = open('/home/mustafa/catkin_ws/test_track.txt', 'r')
    arr = file.readlines()
    for i in range(0, len(arr)):
        arr[i] = arr[i].replace('\n', '')
        
        xy = arr[i].split(',')
        x, y = float(xy[0]), float(xy[1])
        
        t_pose = PoseStamped()
        t_pose.pose.position.x, t_pose.pose.position.y = x, y
        t_pose.header.frame_id = "world"

        t_path.poses.append(t_pose)

def talker():
    pub = rospy.Publisher("target_path", Path, queue_size=10)
    rospy.init_node('path_publisher', anonymous=False)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        t_path.header.frame_id = "world"
        pub.publish(t_path)
        rate.sleep()

if __name__ == '__main__':
    try:
        t_path = Path()
        make_path()
        talker()
    except rospy.ROSInterruptException:
        pass