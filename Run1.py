from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
total = 0
for i in range(100):
    total += hub.battery.voltage()
battery = total / 100
print("\x1b[H\x1b[2J", end="")
print('Battery: ' + str(round((battery-6000)/23)) + '%')
l_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
r_motor = Motor(Port.F)
arm_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
robot = DriveBase(l_motor, r_motor, 56, 159)

robot.settings(
    straight_speed = 180,
    straight_acceleration = 275,
    turn_rate = 150
)
#"""y
while True:
    arm_motor.run(-100)
    print(arm_motor.load())
    if(arm_motor.load() > 30):
        break;

arm_motor.run_angle(100, 30)

robot.use_gyro(True)
robot.straight(20)
robot.turn(90)
robot.straight(520-20)
robot.straight(-105)
robot.turn(-44)
robot.straight(385)
arm_motor.run_angle(100, 160)
robot.turn(-17)
robot.straight(57)
arm_motor.run_angle(100, -150, wait = True);
robot.straight(50);
