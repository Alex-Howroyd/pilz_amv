import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    controller_config = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2/controller/controller.yaml')
    bt_xml_conf = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2/behavior_tree/behavior_tree.xml')
    planner_conf = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2/planner_server/planner_server.yaml')
    recovery_conf = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2/recovery/recovery.yaml')
    bt_navigator_conf = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2/bt_navigator/bt_navigator.yaml')
    waypoint_config = os.path.join(
        get_package_share_directory('pilz_amv'), 'configs/navigation/nav2/waypoint_follower/waypoint_follower.yaml')

    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]

    return LaunchDescription([
        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[controller_config],
            remappings=remappings
        ),     
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[planner_conf],
            remappings=remappings    
        ),
        Node(
            package='nav2_recoveries',
            executable='recoveries_server',
            name='recoveries_server',
            output='screen',
            parameters=[recovery_conf],
            remappings=remappings    
        ),
        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[bt_navigator_conf, {'default_bt_xml_filename': bt_xml_conf}],
            remappings=remappings    
        ),
        Node(
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            name='waypoint_follower',
            output='screen',
            parameters=[waypoint_config],
            remappings=remappings
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager',
            output='screen',
            parameters=[{'autostart': True},
                        {'node_names': ['controller_server',
                                        'planner_server',
                                        'recoveries_server',
                                        'bt_navigator',
                                        'waypoint_follower']}]
        )  
    ])
