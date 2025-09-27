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
    straight_speed = 350,
    straight_acceleration = 200,
    turn_rate = 200
)

arm_motor.run_angle(200, 30)

arm_motor.run_angle(200, -15)

while True:
    arm_motor.run(-100)
    if(arm_motor.load() > 50):
        break;

arm_motor.run_angle(200, 30)

robot.use_gyro(True)
arm_motor.run_angle(100,103.14159265358979323)
robot.straight(530)
robot.straight(-100)
robot.turn(10)
wait(500)
robot.straight(30)
robot.turn(-15)
arm_motor.run_angle(50,-50)
robot.straight(-250)
arm_motor.run_angle(700,-50)
robot.turn(20)
robot.straight(490)
robot.turn(55)
robot.straight(50)
arm_motor.run_angle(100,90)
robot.turn(20)
arm_motor.run_angle(100,30)
robot.straight(70)
arm_motor.run_angle(50,-130, wait = False);
robot.drive(30, 0)
wait(4000)
arm_motor.stop()

robot.straight(100)

arm_motor.run_angle(50, 60);
robot.turn(-30)
robot.straight(170)
robot.turn(50)

robot.straight(120)
robot.turn(50)
robot.straight(167)
robot.turn(50)
robot.straight(-160)
arm_motor.run_angle(100, -60)
