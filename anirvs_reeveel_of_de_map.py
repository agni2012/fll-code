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
time = StopWatch()
robot.use_gyro(True)
#reset arm
while True:
    r_arm_motor.run(-100)
    #print(r_arm_motor.load())
    if(r_arm_motor.load() > 100 or time.time()>2001):
        break;
r_arm_motor.run_angle(100,200)

#move toward mission
robot.straight(600)

#turn to engage into mission
robot.turn(-34)

#move into mission
robot.straight(175)

#raise arm to catch artifact
r_arm_motor.run_angle(100,-150)

#back away from mission
robot.straight(-200)

#turn to exit mission
robot.turn(34)

# back to home
robot.straight(-605)

#ANRIV WHAT IS THIS FOR
robot.turn(-50)
