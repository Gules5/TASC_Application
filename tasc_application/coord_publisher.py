#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32MultiArray

#### Test Data ####

coordinates = Float32MultiArray()
coordinates.data = [43.65891, 79.38083]

#### Test Data End ####

class MyPublisher(Node):
    def __init__(self):
        super().__init__("tasc_publisher")
        self.get_logger().info("SenLocationsor Publisher Created") 

        self.cmd_data_publisher_ = self.create_publisher(Float32MultiArray, "/tasc/data",10)
        self.data_timer = self.create_timer(1, self.sendData)

    def sendData(self):
        self.cmd_data_publisher_.publish(coordinates)    
        self.get_logger().info("Data Sent")                                  


def main(args=None):

    rclpy.init(args=args)

    nodePublisher = MyPublisher() #Declare node

    rclpy.spin(nodePublisher) #Spin node so it stays up
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()