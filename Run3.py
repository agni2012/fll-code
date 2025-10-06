# PortA is right arm motor
# PortB is left arm motor
# PortD is left drive motor
# PortF is right drive motor
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
l_arm_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
r_arm_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
robot = DriveBase(l_motor, r_motor, 56, 159)

robot.settings(
    straight_speed = 500,
    straight_acceleration = 500,
    turn_rate = 150
)
robot.use_gyro(True)
robot.straight(380)

for i in range(5):
    r_arm_motor.run_angle(1000,80)
    r_arm_motor.run_angle(1000,-80)
robot.turn(-26.7)
robot.straight(270)
robot.turn(60)
r_arm_motor.run_angle(50,75)
robot.straight(30)
r_arm_motor.run_angle(50,-75)
