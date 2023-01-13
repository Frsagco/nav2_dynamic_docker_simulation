ARG FROM_IMAGE=frsagco/galactic_webots
ARG OVERLAY_WS=/opt/ros/overlay_ws

######### CLONING #################
# multi-stage for caching
FROM $FROM_IMAGE AS cacher

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
RUN echo "\
repositories: \n\
  navigation2_galactic: \n\
    type: git \n\
    url: https://github.com/Frsagco/nav2_galactic_simulation.git \n\
  nav2_dynamic_bringup: \n\
    type: git \n\
    url: https://github.com/Frsagco/nav2_dynamic_docker_simulation.git \n\
  nav2_dynamic: \n\
    type: git \n\
    url: https://github.com/links-cosero/navigation2_dynamic.git \n\  
  turtlebot3: \n\
    type: git \n\
    url: https://github.com/ROBOTIS-GIT/turtlebot3.git \n\
    version: ${ROS_DISTRO}-devel \n\
  turtlebot3_msgs: \n\
    type: git \n\
    url: https://github.com/ROBOTIS-GIT/turtlebot3_msgs \n\
    version: ${ROS_DISTRO}-devel \n\    
  turtlebot3_dyn: \n\
    type: git \n\
    url: https://github.com/ROBOTIS-GIT/DynamixelSDK.git \n\
    version: ${ROS_DISTRO}-devel \n\    
" > ../overlay.repos
RUN vcs import ./ < ../overlay.repos

# copy manifests for caching
# WORKDIR /opt
# RUN mkdir -p /tmp/opt && \
#     find ./ -name "package.xml" | \
#       xargs cp --parents -t /tmp/opt && \
#     find ./ -name "COLCON_IGNORE" | \
#       xargs cp --parents -t /tmp/opt || true

###### BUILDING ###########
# multi-stage for building
FROM $FROM_IMAGE AS builder

# build overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
COPY --from=cacher $OVERLAY_WS/src ./src
RUN apt-get update &&\
    #apt-get upgrade -y &&\
   # apt install -y ros-dev-tools &&\
    rm -r ./src/navigation2_galactic/nav2_system_tests &&\
    rosdep install -y \
        --from-paths \
            src/nav2_dynamic_bringup \
            src/navigation2_galactic \
        --skip-keys "slam_toolbox" \
        --ignore-src && \
    . /opt/ros/$ROS_DISTRO/setup.sh &&\
    colcon build --packages-select nav2_dynamic_msgs &&\
    colcon build --packages-select turtlebot3_msgs &&\
    . $OVERLAY_WS/install/local_setup.sh &&\ 
    colcon build --packages-skip nav2_dynamic_msgs && \
    cp -r src/nav2_dynamic_bringup/resource/box_obstacle1 /usr/local/webots/projects/default/controllers\
    && rm -rf /var/lib/apt/lists/*


RUN rm src/turtlebot3/turtlebot3_navigation2/param/burger.yaml && \
    cp $OVERLAY_WS/src/nav2_dynamic_bringup/resource/burger.yaml src/turtlebot3/turtlebot3_navigation2/param/ &&\
    . /opt/ros/$ROS_DISTRO/setup.sh && . $OVERLAY_WS/install/local_setup.sh 

# ARG OVERLAY_WS
# WORKDIR $OVERLAY_WS
# COPY --from=cacher /tmp/$OVERLAY_WS/src ./src
# RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
#     apt-get update && rosdep install -y \
#       --from-paths \
#         src/ros2/demos/demo_nodes_cpp \
#         src/ros2/demos/demo_nodes_py \
#       --ignore-src \
#     && rm -rf /var/lib/apt/lists/*


# # build overlay source
# COPY --from=cacher $OVERLAY_WS/src ./src
# ARG OVERLAY_MIXINS="release"
# RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
#     colcon build \
#       --packages-select \
#         demo_nodes_cpp \
#         demo_nodes_py \
#       --mixin $OVERLAY_MIXINS

# # source entrypoint setup
# ENV OVERLAY_WS $OVERLAY_WS
# RUN sed --in-place --expression \
#       '$isource "$OVERLAY_WS/install/setup.bash"' \
#       /ros_entrypoint.sh

# run launch file
CMD [".", "src/nav2_dynamic_bringup/resource/entry_point.sh"]