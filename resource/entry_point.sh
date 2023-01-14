set -e

export TURTLEBOT3_MODEL=burger

ros2 launch nav2_dynamic_bringup robot_rplidar_launch.py world:=turtlebot3_rplidar_obstacle.wbt &
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$oVERLAY_WS/src/nav2_dynamic_bringup/resource/map.yaml.yaml &
ros2 launch nav2_dynamic_bringup nav2_launch.py &

ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped '{
    "header": { "frame_id": "map" },
    "pose": {
        "pose": {
            "position": { "x": 3.39574, "y":  -0.00357813, "z": 0.0 },
            "orientation": { "x": 0.0, "y": 0.0, "z": -0.999999, "w":  0.0016893 }
        }
    }
}'

read


exec "$@"
