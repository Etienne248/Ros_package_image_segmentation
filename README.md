# ROS Package for PyTorch Image Segmentation
This ROS package performs image segmentation using PyTorch and runs in a Docker container. The package includes one node, "pytorch_seg", which subscribes to the topic "image", processes the image, generates a segmentation mask, and publishes it on the topic "segMask". The package also includes two test nodes: the node "camera" gets images from the webcam and publishes them on the "image" topic, and the "mask_processing" node subscribes to the "segMask" topic and displays the segmentation mask.

## Installation
Clone this repository to your machine

```bash
git clone https://github.com/Etienne248/Ros_package_image_segmentation.git
```
Build the Docker container using the Dockerfile provided
```bash
docker build -t ros-segmentation .
```
## Usage
Run the Docker container
```bash
docker run --rm -it --name ros-segmentation-container ros-segmentation
```
Launch the ROS nodes

```bash
roslaunch ros_segmentation all.launch
```

Launch the test nodes

```bash
roslaunch ros_segmentation test.launch
```

## Nodes
### pytorch_seg
This node subscribes to the "image" topic, processes the image using PyTorch, generates a segmentation mask, and publishes it on the "segMask" topic.

Subscribed Topics  
* /image (sensor_msgs/Image)  
   The image to be segmented.

Published Topics  
* /segMask (sensor_msgs/Image)  
  The segmentation mask generated from the input image.  

### camera
This node captures images from the webcam and publishes them on the "image" topic.

Published Topics  
*   /image (sensor_msgs/Image)  
    The images captured from the webcam.

### mask_processing
This node subscribes to the "segMask" topic and displays the segmentation mask.

Subscribed Topics
*   /segMask (sensor_msgs/Image)  
    The segmentation mask to be displayed.

