import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace
from nav2_common.launch import RewrittenYaml


def generate_launch_description():
    # Get the launch directory
    costmap_to_dynamic_dir = get_package_share_directory('ros2_costmap_to_dynamic_obstacles')
    kf_hungarian = get_package_share_directory('kf_hungarian_tracker')

    launch_dir_kf = os.path.join(kf_hungarian, 'launch')

    # Specify the actions
    bringup_cmd_group = GroupAction([
        Node(
            name='my_converter_node',
            package='ros2_costmap_to_dynamic_obstacles',
            executable='my_converter_node',
            output='screen'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir_kf, 'kf_hungarian.launch.py'))),
    ])

    # Create the launch description and populate
    ld = LaunchDescription()

    # Add the actions to launch all of the navigation nodes
    ld.add_action(bringup_cmd_group)

    return ld
