
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
  
    robot_description_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'),'configs/robot_description/robot_description.launch.py')
  
    rviz_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'),'configs/rviz/rviz.launch.py')
    
    kinematics_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'),'configs/kinematics/kinematics.launch.py')
    
    teleop_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'),'configs/teleop/teleop.launch.py')
    
    psen_scan_v2_launch_file = os.path.join(
        get_package_share_directory('psen_scan_v2'),'launch/bringup.launch.xml')
      
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([robot_description_launch_file])),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([rviz_launch_file])),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([kinematics_launch_file])),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([teleop_launch_file])),

        IncludeLaunchDescription(
            XMLLaunchDescriptionSource([psen_scan_v2_launch_file])),

        Node(
            package="pilz_amv",
            executable="joint_states.py",
            name='joint_states'
        )
  	])