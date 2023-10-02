import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    slam_conf = LaunchConfiguration('parameters', default=os.path.join(
        get_package_share_directory('pilz_amv'),'configs/navigation/slam/slam.yaml'))

    return LaunchDescription([
        DeclareLaunchArgument(
            'parameters',
            default_value=slam_conf,
            description='Full path to param file to load'),

        Node(
            package='slam_toolbox', 
            executable='sync_slam_toolbox_node', 
            output='screen',
            name='slam_toolbox', 
            parameters = [slam_conf])
    ])
