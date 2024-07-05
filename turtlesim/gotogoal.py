#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import sys


self_pose = Pose()
def pose_callback(msg: Pose):
    global self_pose
    self_pose = msg

rospy.init_node("GTG", anonymous = True)
sub = rospy.Subscriber('turtle1/pose',Pose, callback = pose_callback)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

def gtg():
    goal = Pose()
    goal.x = float(sys.argv[1])
    goal.y = float(sys.argv[2])

    new_vel=Twist()
    rate= rospy.Rate(10)

    while(True):
        dist2g = math.sqrt((goal.x - self_pose.x)**2 + (goal.y - self_pose.y)**2)
        ang2g = math.atan2(goal.y - self_pose.y, goal.x - self_pose.x)

        angle_error = ang2g - self_pose.theta

        new_vel.angular.z = 2 * angle_error
        new_vel.linear.x = 0.5 * dist2g

        if dist2g < 0.1:
            new_vel.linear.x = 0
            new_vel.angular.z = 0
            rospy.loginfo("Goal reached.")
            break
                
        ##rospy.loginfo( "DTG : {:3f} , ATG : {:3f} , Aerr : {:3f}" .format(dist2g,ang2g,angle_error))    
        pub.publish(new_vel)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.loginfo("Locating goal...")
        gtg()
        
    except rospy.ROSInterruptException:
        pass