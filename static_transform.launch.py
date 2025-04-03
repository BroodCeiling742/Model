from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
     Node(
         package= 'tf2_ros',
         executable= 'static_transform_publisher',
         arguments= ['1.0', '2.0', '3.0', '0.0', '0.0', '0.0', '1.0', 'world', 'base_link'],
     )   
    ])
