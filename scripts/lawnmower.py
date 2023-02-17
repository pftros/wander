#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Lawnmower:

    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist)
        self.sub = rospy.Subscriber('odom', Odometry, self.odom_callback, queue_size=1)
        self.cmd_vel = Twist()

    def odom_callback(self, odom):
        rospy.loginfo(f'x: {odom.pose.pose.position.x}')
        self.cmd_vel.linear.x = 0.1
        if odom.pose.pose.position.x > 1:
            self.cmd_vel.linear.x = 0
        self.pub.publish(self.cmd_vel)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('lawnmower')
    mower = Lawnmower()    
    mower.run()
