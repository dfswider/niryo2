from pyniryo import *
f = open("points_saved.txt", "a")

robot = NiryoRobot("192.168.6.50")

pos = robot.get_pose()
print(pos)
f.write(str(pos))
f.write("\n")

robot.close_connection()
