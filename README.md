All staff necessary to run a simple docker simulation. 

ROS2 Version: Galactic. Simulator: Webots 2023a

The simulation can be visualized executing these commands:
 - xhost +local:
 - docker run -it --rm -e DISPLAY=$DISPLAY --network host -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/dri:/dev/dri frsagco/nav2_dynamic_simulation

If webots and RVIZ does not open properly just try to execute this command:
 - sudo docker run -it --rm --privileged -e DISPLAY=$DISPLAY --network host -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/dri:/dev/dri frsagco/nav2_dynamic_simulation