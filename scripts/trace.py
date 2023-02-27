#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from visualization_msgs.msg import Marker

class Trace:

    def __init__(self):
        self.pub_marker = rospy.Publisher('trace',Marker, queue_size=1)
        self.sub = rospy.Subscriber('odom', Odometry, self.odom_callback, queue_size=1)
        self.trace = Marker()
        self.trace.pose.orientation.w = 1
        self.trace.type = Marker.LINE_STRIP
        self.trace.color.r = 1
        self.trace.color.a = 1
        self.trace.scale.x = 0.1
        self.trace.scale.y = 0.5
        
    def odom_callback(self, odom):
        self.trace.header = odom.header
        self.trace.points.append(odom.pose.pose.position)
        self.trace.colors.append(self.trace.color)
        self.pub_marker.publish(self.trace)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('trace')
    mower = Trace()    
    mower.run()
