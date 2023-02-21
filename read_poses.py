from pyniryo import *

robot = NiryoRobot("192.168.6.50")

pos = robot.get_pose()
print(pos)

robot.close_connection()
