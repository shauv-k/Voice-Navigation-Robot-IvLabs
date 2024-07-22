# Voice-Navigation-Robot-IvLabs

## Requirements

* Ubuntu 20.04
* ROS Noetic
* Pocketsphinx
* Gstreamer

## Turtlesim

Turtlesim is an inbuilt package in ROS that provides a 2D simulation environment to experiment with various ROS concepts. We tested various tasks in turtlesim such as trajectories, go to goal behaviour and such to learn ROS concepts. The goal was to create various publisher node over the required topics to acheive the required task.  

[ROS Noetic Installation](https://wiki.ros.org/noetic/Installation/Ubuntu)  
[ROS Tutorials](https://drive.google.com/drive/folders/1w25DNhHX5ni11rzTHJScpawzCPzLkVGt?usp=sharing)

## Gazebo

Gazebo is a robotics simulation environment included within ROS. It provides a 3D physics-based simulation of robots, environments, and sensors, allowing users to simulate and test robotic systems in a virtual environment before deploying them in the real world.  

[Gazebo Tutorials](https://classic.gazebosim.org/tutorials)

## Turtlebot 3

TurtleBot 3 is a versatile open source robot platform designed for education, research, and prototyping applications in robotics. It is fully compatible with ROS, making it easy to integrate with ROS-based software libraries, tools, and simulations allowing users to leverage the extensive ROS ecosystem for developing and testing robotic applications.

[Turtlebot 3 Manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

INSTALLATION:
1) Run the following commands in your terminal. Make sure to clone the repositories into your workspace.
   ```
   git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
   git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
   git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
   ```
2) Build your packages.
   ```
   catkin_make
   ```

BASIC SIMULATION:
1) Export your turtlebot model. We will be using burger.
   ```
   export TURTLEBOT3_MODEL=burger
   ```
2) To launch and empty world use the following command.
   ```
   roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
   ```
3) To launch another world with objects use the following command.
   ```
   roslaunch turtlebot3_gazebo turtlebot3_world.launch
   ```
4) To perform teleoperations open another terminal and run the following.
   ```
   nd ort TURTLEBOT3_MODEL=burger
   roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
   ```
   
## Pocketsphinx

PocketSphinx is a lightweight speech recognition engine developed by Carnegie Mellon University (CMU). We will be using pocketsphinx for the purpose of speech recognition and voice control of the robot.

INSTALLATION:
1) Clone the [pocketsphinx](https://github.com/cmusphinx/pocketsphinx) and [sphinxbase](https://github.com/cmusphinx/sphinxbase) repostories into your workspaces.
2) Go into the sphinxbase folder and build it.

   ```
   ./autogen.sh
   ./configure
   make
   make install
   ```

## Gstreamer

GStreamer is a multimedia framework that provides a pipeline-based architecture for constructing multimedia applications. It is open source and widely used in various applications and platforms to handle multimedia processing, streaming, and playback. We will be using gstreamer to integrate pocketsphinx into our ROS project.

INSTALLATION:  

```
apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```
