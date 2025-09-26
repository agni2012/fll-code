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

arm_motor.run_angle(200, 30)

arm_motor.run_angle(200, -15)

while True:
    arm_motor.run(-100)
    if(arm_motor.load() > 50):
        break;

arm_motor.run_angle(200, 30)

robot.use_gyro(True)
arm_motor.run_angle(100,102.5)
robot.straight(530)
robot.straight(-100)
robot.turn(10)
wait(500)
robot.straight(30)
robot.turn(-15)
arm_motor.run_angle(100,-50)
robot.straight(-250)
arm_motor.run_angle(100,-50)
robot.turn(20)
robot.straight(580)
robot.turn(60)
robot.straight(50)
arm_motor.run_angle()
robot.turn(20)
robot.straight(200)
