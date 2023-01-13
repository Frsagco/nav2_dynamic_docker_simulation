FROM ros:galactic

# installing webots
RUN apt-get update &&\ 
    apt-get install -y software-properties-common &&\
    apt-get install -y wget &&\ 
    wget -qO- https://cyberbotics.com/Cyberbotics.asc | apt-key add - && \
    apt-add-repository 'deb https://cyberbotics.com/debian/ binary-amd64/' &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y webots


RUN apt-get install -y ros-$ROS_DISTRO-webots-ros2 &&\
    apt-get -y install python3-pip &&\
    cd opt/ros/galactic/share/webots_ros2_importer &&\
    git clone https://github.com/cyberbotics/urdf2webots.git && \
    cd urdf2webots && pip3 install -r requirements.txt &&\
    apt-get install -y ros-$ROS_DISTRO-bondcpp &&\
    apt-get install ros-$ROS_DISTRO-test-msgs &&\
    apt-get install python3-opencv \
    && rm -rf /var/lib/apt/lists/*

