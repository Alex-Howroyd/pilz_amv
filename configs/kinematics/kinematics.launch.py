import launch
import launch.actions
import launch.substitutions
import os
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions

def generate_launch_description():
    config = os.path.join(get_package_share_directory('pilz_amv'),'configs/kinematics','kinematics.yaml')
    robot_namespace = launch.substitutions.LaunchConfiguration('namespace', default="")

    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='kinematics_differential',
            executable='differential_node',
            output='screen',
            namespace = robot_namespace,
            name='differential_node',
            parameters = [config])
    ])