FROM osrf/ros:noetic-desktop-full

# Update all packages
RUN apt update && apt upgrade -y

# Install Git
RUN apt install -y git python3-pip xauth

# Rosdep update
RUN rosdep update

# Install cv2
RUN python3 -m pip install --upgrade opencv-python 

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN echo "source /workspace/Ros_package_image_segmentation/catkin_ws/devel/setup.bash" >> ~/.bashrc

