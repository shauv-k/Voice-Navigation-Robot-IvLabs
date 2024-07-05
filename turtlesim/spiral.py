#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def spiral():
    rospy.init_node("Spiral", anonymous = True)
    spiral_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    
    ang_vel = 5.0
    lin_vel = 0
    while not rospy.is_shutdown():
        trajectory = Twist()
        trajectory.linear.x = 0.1 + lin_vel
        trajectory.angular.z = ang_vel
        lin_vel += 0.1
        ang_vel = ang_vel - 0.1
        if ang_vel <= 0 :
            break
        spiral_pub.publish(trajectory)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.loginfo("Making a spiral...")
        spiral()
    except rospy.ROSInterruptException:
        pass
    