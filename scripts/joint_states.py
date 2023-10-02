#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory

class JointStatesPub(Node):
	def __init__(self):
			super().__init__('joint_states_pub')
			self.joint_state_pub = self.create_publisher(JointState, '/drives/joint_states', 10)
			self.joint_trajectory_sub = self.create_subscription(JointTrajectory, '/drives/joint_trajectory', self.joint_trajectory_callback, 10)
			self.timer = self.create_timer(0.01, self.update_odom)
			self.right_vel = 0.0
			self.left_vel = 0.0
			
	def joint_trajectory_callback(self, msg):
			self.right_vel = msg.points[0].velocities[0]
			self.left_vel = msg.points[0].velocities[1]
        
	def update_odom(self):
			joint_state = JointState()
			joint_state.header.stamp = self.get_clock().now().to_msg()
			joint_state.name = ['fixed_wheel_right_joint','fixed_wheel_left_joint']
			joint_state.position = [0.0, 0.0]
			joint_state.velocity = [self.right_vel, self.left_vel]
			self.joint_state_pub.publish(joint_state)
   
def main(args=None):
    rclpy.init(args=args)
    joint_states_pub = JointStatesPub()
    rclpy.spin(joint_states_pub)
    joint_states_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()