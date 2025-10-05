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
    straight_speed = 400,
    straight_acceleration = 300,
    turn_rate = 200
)
robot.use_gyro(True)
l_arm_motor.run_target(100,170)
robot.straight(540)
robot.straight(-110)
robot.turn(10)
wait(500)
robot.straight(30)
robot.turn(-15)
l_arm_motor.run_angle(50,-50)
robot.straight(-250)
l_arm_motor.run_angle(700,-50)
robot.turn(20)
robot.straight(490)
robot.turn(55)
robot.straight(50)
l_arm_motor.run_angle(100,90)
robot.turn(20)
robot.straight(70)
l_arm_motor.run_angle(50,-130, wait = False);
robot.drive(30, 0)
wait(4000)
l_arm_motor.stop()

robot.straight(100)

l_arm_motor.run_angle(50, 60);
robot.turn(-30)
robot.straight(200)
robot.turn(45)
robot.straight(280)
robot.turn(22)
robot.settings(straight_speed=100)
robot.straight(150)
robot.settings(straight_speed=400)
robot.straight(-200)

robot.turn(30)
robot.straight(200)
robot.turn(10)
robot.straight(-200)
