#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def path(pub,rate):
    trajectory = Twist()
    trajectory.linear.x = 4.0
    pub.publish(trajectory)
    rate.sleep()
    trajectory.linear.x = 0.0
    pub.publish(trajectory)
    rate.sleep()
    trajectory.angular.z = 3.14159265358979323846/2
    pub.publish(trajectory)
    rate.sleep()
        
def square():
    rospy.init_node("Circle", anonymous = True)
    sq_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
       path(sq_pub,rate)
        

if __name__ == '__main__':
    try:
        rospy.loginfo("Making a circle...")
        square()
    except rospy.ROSInterruptException:
        pass
    