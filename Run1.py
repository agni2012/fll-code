def run1():
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
        straight_speed = 500,
        straight_acceleration = 700,
        turn_rate = 200
    )

    arm_motor.run_angle(200, 30)

    arm_motor.run_angle(200, -15)

    while True:
        arm_motor.run(-100)
        if(arm_motor.load() > 50):
            break;

    arm_motor.run_angle(40, 28)

    robot.use_gyro(True)
    arm_motor.run_angle(70,102.14159265358979323846264338327950288)
    
    arm_motor.hold();
    wait(1000);
    #brush mission
    robot.straight(530)
    robot.straight(-55, then = Stop.NONE)

    robot.straight(-40, wait = False)
    arm_motor.run_angle(170,-25, wait = False)
    robot.straight(-255)

    robot.straight(300, then =  Stop.NONE)
    robot.settings(
        straight_speed = 200
    )

    arm_motor.run_angle(170,25, wait = False)
    robot.arc(147, angle = 90, then = Stop.NONE)
    robot.settings(
        straight_speed = 500
    )

    arm_motor.run_angle(170,-105, wait = False)
    #whats on the scale
    robot.straight(175)
    robot.turn(-10)

    robot.straight(200)
    robot.turn(-20)
    robot.straight(200)
    robot.turn(45)
    robot.straight(280)
    robot.turn(22)
    robot.settings(straight_speed=100)
    robot.straight(170)
    robot.settings(straight_speed=400)
    robot.straight(-200)

    robot.turn(10)

    robot.turn(50)

    robot.straight(150)
    arm_motor.run_angle(200, -100,wait=False)
    wait(500)
    arm_motor.run_angle(100, 100, wait = False)
    robot.settings(straight_acceleration=1000)
    robot.settings(straight_speed=700)
    robot.arc(400, angle=70, then = Stop.NONE)
    robot.arc(-1000, distance=700)
