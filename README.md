# Elephant myAGV ROS2 full python package 
This package is ROS2 full python package for Elephant robotics myAGV autonomous vehicle. 

## Operating vehicle
### Tunr on lidar
At first you need to turn on Raspberry pi GPIO 20. myAGV hardware need such action. 
To turn on lidar, execute following script. 

```
pi@pi:~/myagv_ws$ sudo python3 src/myagv_node/myagv_node/lidar_on.py
```

### Turn off lidar 
To turn off lidar, execute following script.
```
pi@pi:~/myagv_ws$ sudo python3 src/myagv_node/myagv_node/lidar_off.py
```

### To view URDF on rViz
To view myAGV URDF file on rViz, execute follwing launch script. 
```

```

To operate myAGV wheel, execute follwoing launch script.
```
pi@pi:~/myagv_ws$ ros2 launch myagv_bringup myagv_launch.py
```

And open another terminal, execute follwing teleop node. 
```
pi@pi:~/myagv_ws$ ros2 run teleop_twist_keyboard  teleop_twist_keyboard
```
You can operate vehicle wheel using some keys. 
