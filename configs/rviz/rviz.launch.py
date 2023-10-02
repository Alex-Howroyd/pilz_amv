
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

  rviz_config_path = PathJoinSubstitution([FindPackageShare('pilz_amv'), 'configs/rviz/nav2_default_view.rviz'])
      
  return LaunchDescription([
			Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]
        )
  	])