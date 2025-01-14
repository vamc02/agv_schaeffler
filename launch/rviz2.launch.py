from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Define the path to your RViz configuration file
    rviz_config_file = os.path.join(
        os.getenv('HOME'),'Documents','thesis_ssh_work', 'agv', 'src', 'agv_schaeffler', 'config', 'drive_agv_lidar.rviz'
    )

    # Create an RViz2 Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    # Return the Launch Description
    return LaunchDescription([rviz_node])
