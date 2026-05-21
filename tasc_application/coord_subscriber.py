#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32MultiArray
                        

class MySubscriber(Node):
    def __init__(self):
        super().__init__("tasc_subscriber")
        self.get_logger().info("Location Subscriber Created")

        self.tasc_subscriber_ = self.create_subscription(Float32MultiArray,"/tasc/data", self.pose_callback, 10)

    def pose_callback(self, msg:Float32MultiArray):
        self.get_logger().info("Longitude: " + str(msg.data[0]) + " Latitude: " + str(msg.data[1]) )


def main(args=None):

    rclpy.init(args=args)


    nodeSubscriber = MySubscriber() #Declare node

    rclpy.spin(nodeSubscriber)#Spin node so it stays up
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()