#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#import Robotiranyitas

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#főprogram
#robotom=Robotiranyitas():


# Create your objects here.
ev3 = EV3Brick()
bm = Motor(Port.B)
jm = Motor(Port.C)
km = Motor(Port.A)




# Sensor
us = UltrasonicSensor(Port.S4)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)
gs = GyroSensor(Port.S2)


# Motor kezelés
robot = DriveBase(jm, bm, 56, 132)



# Write your program here.

#Robot irányítása
robot.straight(200)
wait(1)
robot.straight(-200)
robot.turn(90)
robot.turn(-90)


ev3.speaker.beep()

