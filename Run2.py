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
    straight_speed = 700,
    straight_acceleration = 500,
    turn_rate = 150
)
#"""y
while True:
    arm_motor.run(-100)
    print(arm_motor.load())
    if(arm_motor.load() > 30):
        break;

arm_motor.run_angle(200, 30)

robot.use_gyro(True)
robot.settings(straight_acceleration=500);
robot.straight(420, then = Stop.COAST_SMART);
robot.settings(straight_acceleration=150);
robot.straight(80);
robot.straight(-100);
robot.turn(-39.2);
robot.settings(straight_acceleration=700);
arm_motor.run_angle(70, 100, wait=False);
robot.straight(235, then = Stop.NONE);
arm_motor.stop();
arm_motor.run_angle(470, 110, wait = False);
robot.straight(170);
robot.turn(-12);
arm_motor.stop();

robot.straight(90);#p90
robot.turn(-1);
arm_motor.run_angle(100, -100, wait = False);
robot.settings(straight_acceleration=150)
robot.straight(-45);
robot.straight(34);

robot.settings(straight_acceleration=300);
robot.turn(57);#
robot.straight(208);

robot.settings(straight_acceleration=700);
robot.settings(turn_acceleration=150)
robot.settings(turn_rate=150)
robot.turn(30);
robot.straight(650);

arm_motor.run_angle(100, -100)
