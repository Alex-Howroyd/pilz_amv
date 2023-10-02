import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    amcl_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/amcl')
    
    nav2_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2')
    
    display_amv_launch_file = os.path.join(
        get_package_share_directory('pilz_amv'), 'launch')
    
    return LaunchDescription([

        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="screen" ,
            arguments=["0", "0", "0", "0", "0", "0", "map", "odom"]
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([display_amv_launch_file, '/display_amv.launch.py'])
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file, '/nav2.launch.py'])
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([amcl_launch_file, '/amcl.launch.py'])
        )
        
    ])