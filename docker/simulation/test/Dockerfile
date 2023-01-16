ARG FROM_IMAGE=frsagco/galactic_webots
ARG OVERLAY_WS=/opt/ros/overlay_ws

######### CLONING #################
# multi-stage for caching
FROM $FROM_IMAGE AS cacher

# clone overlay source
ARG OVERLAY_WS
ENV OVERLAY_WS=$OVERLAY_WS

ENTRYPOINT ["/ros_entrypoint.sh"]

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
