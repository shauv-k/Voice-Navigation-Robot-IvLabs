#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def circle():
    rospy.init_node("Circle", anonymous = True)
    circle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        trajectory = Twist()
        trajectory.linear.x = 2.0
        trajectory.angular.z = 1.0
        circle_pub.publish(trajectory)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.loginfo("Making a circle...")
        circle()
    except rospy.ROSInterruptException:
        pass
    