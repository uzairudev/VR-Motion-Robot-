# VR Motion Robot

This project integrates a VR-based interface with a robotic turtle simulation in ROS (Robot Operating System). It aims to explore how virtual reality can be used to control motion robots in real-time and to synchronize human movements with robot actions in a simulated or physical environment.

## Project Overview

The project involves using a VR headset to detect and map the motion of a subject (user) onto a simulated robot. The robot's movements are controlled through Python and C++ programs, while Unity is used for visualization. This technology could be applied in various industries, from manufacturing to medical robots, especially for teleoperation in hazardous environments.

### Key Objectives:
- Provide an immersive VR interface for robot control.
- Synchronize human movement with robotic actions.
- Demonstrate robot control in a simulated environment with TurtleSim.

### Tools and Devices

1. **VR Headset** – For detecting user movements.
2. **TurtleSim** – A 2D simulator used to visualize and test the robot's movements.
3. **Unity** – The platform used to visualize the robot in a VR environment.
4. **ROS (Robot Operating System)** – The middleware handling communication between the VR environment and the robot.

### Implementation Steps

1. **Detect the subject’s position** using the VR headset.
2. **Gather position data** from the VR system.
3. **Synchronize movement** with the robot by reshaping the data using a Python script, converting it to velocity and angular data.

### Project Files

- **turtle.cpp & turtle.h**: Handle the turtle's movement and ROS communication.
- **turtleMove.py**: Reads movement data from CSV files and sends control commands to the turtle in ROS.
- **roboticsProject.launch**: The launch file that starts the ROS TurtleSim node and the movement control script.
- **Unity Folder**: Contains Unity-based scripts that visualize the robot's motion in a VR setting.

### Technical Challenges

1. **VR Headset Compatibility**: The initial VR equipment was incompatible with our system, requiring troubleshooting and setup adjustments.
2. **ROS Installation**: Setting up ROS on a virtual machine failed, and we had to install Linux on a separate partition to run ROS successfully.

### Results

We successfully synchronized human movement (captured via VR) with a simulated turtle robot. The movement in VR was reflected in real-time in the TurtleSim environment, demonstrating the feasibility of controlling robots using VR.



