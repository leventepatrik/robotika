


class Robotiranyitas():
    def __init__(self):

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

def forudla(self):
    robot.speed(10/S1)
    robot.drive(100,0)

def fordulb(self):
    pass

def forculc(self):
    pass


