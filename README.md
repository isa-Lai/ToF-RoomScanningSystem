# ToF-RoomScanningSystem
Taking light sensor and motor to generate a 360 degree 3D graph file. Mcmaster University COMPENG 2DX4 final project.


## General Information

This measurement system is used to acquire the information of the layout of the area around this system.  The distance data is acquired with **VL53L1X** light sensor.  The sensor is attaching to **28BYJ-48** motor to give a 360-degree of measurement angle, and it measured in geometric z-y plan.  Multiple rotations of measurement are allowed with manually move the device 15cm after each rotation in x-axis. The information will stored in **TI MSP432E401Y** MCU memory and send to PC, so PC can map each data of point and plot the 3D graph of layout. 

***For more information please refer to the datasheet file ***

## Device 

* Texas Instrument MSP432E401Y
* 28BYj-48 Stepper Motor & ULN2003 Stepper Motor Driver
* VL53L1X Time-of-Flight Sensor
* PC with **Python 3** and **Open3D**, **PySerial**, and **NumPy** packages. 

## To Use this System

To use this system, push reset to start the initializing process. After initialization, run Python file and push PJ1 onboard button to start measuring. After each rotation, manually move the device and push PJ1 again for measurement of another rotation. If the complete measurement is done, push PJ0 onboard button to stop.  The 3D graph will automatically appear in the screen. 

**Detailed steps in listed in *Applicationo Example* section of datasheet file.**

## Special Note Regards to Mcmaster Course

**Do Not** copy any code from this repository.

Please follow the Mcmaster Academic Integrity Policy and the Code of Conduct of the Professional Engineers of Ontario.

