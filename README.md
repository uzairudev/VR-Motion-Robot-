# VR Motion Robot

This project integrates a VR-based interface with a robotic turtle simulation in ROS (Robot Operating System). It utilizes both Python and C++ to manage robot motion, and Unity is used to provide a graphical interface for controlling the robot.

## Project Overview

The project simulates a robotic turtle that moves within a 2D space using ROS. The turtle's movement can be controlled via a set of Python and C++ scripts, and the simulation environment is visualized using Unity. The primary goal of the project is to allow motion control of the turtle from a VR setup.

### Key Components

1. **TurtleSim Node (C++)**: Manages the turtle's movement and ROS communication, including subscribing to velocity commands, publishing the turtle's pose, and handling teleportation requests.
2. **turtleMove.py (Python)**: The Python script that publishes velocity commands to control the turtle's movement. It reads a set of predefined trajectories from CSV files and publishes corresponding movement commands to the turtle.
3. **Unity Visualization (C#)**: Provides a graphical interface for controlling the robot using VR motion. The Unity code publishes turtle pose data to ROS topics for real-time visualization.

### Project Files

- **turtle.cpp & turtle.h**: These files handle the movement of the turtle within the simulation. They implement services like setting the turtle's pen, teleporting, and publishing the pose.
- **turtleMove.py**: This Python script reads movement data from CSV files, calculates velocities and angles, and publishes these values to control the turtle's movement.
- **roboticsProject.launch**: The ROS launch file that starts the turtle simulation and the `turtleMove` node.
- **Unity Folder**: Contains Unity-based code to integrate the simulation with VR and visualize the robot's movement in a 3D space.
  

### How It Works

- **ROS Turtle Simulation**: The turtle starts at a predefined position and receives velocity commands to move along specific trajectories defined in CSV files. These commands are published by the `turtleMove.py` script.
- **Unity Visualization**: The Unity interface shows the real-time movement of the turtle based on the data from ROS. You can visualize and interact with the turtle in a VR environment.

### CSV Data Structure

- The CSV files contain the data required for the turtle's movement, including:
  - Time (seconds and nanoseconds)
  - X and Y coordinates
  - Rotation angles
