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
arm_motor.run_angle(100,100.14159265358979323)

#brush mission
robot.straight(530)
robot.straight(-100)
robot.turn(10)
wait(500)
robot.straight(30)
robot.turn(-15)
arm_motor.run_angle(50,-50)
robot.straight(-250)
arm_motor.run_angle(70,-50)

#Aayana (mineshaft explorer)
robot.turn(20)
robot.straight(490)
robot.turn(55)
robot.straight(50)
arm_motor.run_angle(100,90)
robot.turn(20)
arm_motor.run_angle(100,35)
robot.straight(75)
arm_motor.run_angle(50,-130, wait = False);
robot.drive(29, 0)
wait(4000)
arm_motor.stop()

#whats on the scale
robot.straight(105)
arm_motor.run_angle(50, 60, wait=False);
robot.turn(-30)
robot.straight(200)
robot.turn(45)
robot.straight(280)
robot.turn(22)
robot.settings(straight_speed=100)
robot.straight(150)
robot.settings(straight_speed=400)
robot.straight(-200)

#tip the scale
robot.turn(90)
robot.straight(60) #was 150
robot.turn(-30)
robot.straight(-80) #was 60
robot.turn(-20)
arm_motor.run_angle(300,-90)
