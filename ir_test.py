from pyniryo2 import *

robot = NiryoRobot("192.168.6.50")
for i in range(0, 10):
    print(robot.io.get_digital_io_state(PinID.DI5))
    robot.wait(2)
robot.end()


