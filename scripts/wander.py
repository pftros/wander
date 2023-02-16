#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3, Twist
from sensor_msgs.msg import LaserScan

class wander:

    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist)
        self.sub = rospy.Subscriber('base_scan', LaserScan, self.scan_callback, queue_size=1)
        self.vel_cmd = Twist()

    def scan_callback(self, scan):
        closest = min(scan.ranges)
        rospy.loginfo(f'Closest range: {closest}')
        self.vel_cmd.angular.z = 0.3
        self.pub.publish(self.vel_cmd)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('wander')
    controller = wander()    
    controller.run()
