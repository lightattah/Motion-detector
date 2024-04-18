# Motion Detector Project
## Project Overview
This project is a motion detection system that uses a webcam to detect moving objects and logs the time of movement. It also provides a visual representation of the motion events over time using a dynamic graph.

## Features
Real-Time Motion Detection: Utilizes the webcam to detect motion in real-time.
Event Logging: Records the times at which motion occurs.
Visual Analytics: Generates a time plot of motion events using Bokeh, which can be interacted with to view specific timestamps.
How It Works
The motion_detector.py script captures video from the webcam, processes the video frames to detect motion, and logs the entry and exit times of motion. The plotting.py script reads this data and generates a graphical timeline of the events.

## Technologies Used
Python
OpenCV for video processing and motion detection.
Pandas for data manipulation.
Bokeh for generating interactive plots.
Getting Started
Prerequisites
Python 3.9
OpenCV
Pandas
Bokeh
You can install the necessary libraries using pip:
pip install opencv-python-headless pandas bokeh

## Installation
Clone the repository:
git clone https://github.com/lightattah/Motion-detector
Navigate to the project directory:
cd main
Running the Application
Run the motion detection script:
python motion_detector.py
Open another terminal and run the plotting script to view the motion events graphically:
python plotting.py
Files
motion_detector.py: Contains the logic for video capture, frame processing, motion detection, and data logging.
plotting.py: Uses the data logged by the motion detector to plot a timeline of motion events.

## Author
Light Attah
