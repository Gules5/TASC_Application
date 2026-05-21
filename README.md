Hello!

This is my application for the TASC Communication and Controls Subteam. This is my first time making a ROS2 project, apologies if the github setup isn't standard.

In this project I decided to send and recieve GPS coordinates in longitude and latitude pairs. I sent this data using the built-in Float32MultiArray datatype in ros2.
When the data is recived it is formatted and logged in the terminal, this can be seen in the attached screenshot "node_communication.png", and the connection
between the nodes can be seen in "rqt_graph.png" which is an rqt graph.

In a robotics system the robot would be publishing its location data so that other components of the system can know where the robot is at any given time. The main use
of this would be in navigation. The robot must know its current position in order for it to know where it needs to go and how it should move to get there.


To build the project: 
colcon build --symlink-install

To run the publisher and subscriber nodes respectively:
ros2 run tasc_application coord_publisher
ros2 run tasc_application coord_subscriber
