from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
l_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
r_motor = Motor(Port.C)
robot = DriveBase(l_motor, r_motor, 56, 159)

robot.settings(
    straight_speed = 275,
    straight_acceleration = 200,
    turn_rate = 200
)
robot.use_gyro(True)
robot.straight(305, then=Stop.NONE)
robot.straight(-160)
