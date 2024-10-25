from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState, LaserScan
from rclpy.clock import ROSClock
from rclpy.time import Time
from rclpy.node import Node
from std_msgs.msg import String
import rclpy
import random
import serial
import threading 
import struct
import time 

class jdamr_driver(Node): 
    def __init__(self):
        super().__init__('joint_state_publisher')

        # Create a publisher that will publish to the /joint_states topic
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
    
        # Set a timer to publish at a specified rate (1 Hz in this case)
        self.timer = self.create_timer(0.05, self.publish_joint_states)
        
        # Initialize the JointState message
        self.joint_state = JointState()
        self.joint_state.name = ['wheel1_joint', 'wheel2_joint']
        self.joint_state.position = [0.0, 0.0]
        
        self.position = 0.0
    

    def publish_joint_states(self):
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        
        # Update the joint positions (here, we use a simple oscillation function)
        self.joint_state.position[0] = self.position
        self.joint_state.position[1] = self.position

        # Log the joint positions for debugging
        self.get_logger().info(f'Publishing joint positions: {self.joint_state.position}')

        # Publish the JointState message
        self.publisher_.publish(self.joint_state)


def main(args=None):
    rclpy.init(args=args)
    driver = jdamr_driver()
    rclpy.spin(driver)
    driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()