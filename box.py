from pyniryo import *

robot = NiryoRobot("192.168.6.50")

robot.calibrate_auto()
robot.update_tool()

point = PoseObject(x = 0.1303, y = 0.0150, z = 0.1948, roll = 0.267, pitch = 1.514, yaw = 0.426)
robot.move_pose(point)
point = PoseObject(x = 0.3013, y = -0.0837, z = 0.0313, roll = -2.337, pitch = 1.547, yaw = -2.451)
robot.move_pose(point)
point = PoseObject(x = 0.2893, y = 0.1251, z = 0.0095, roll = -2.662, pitch = 1.479, yaw = -1.869)
robot.move_pose(point)
point = PoseObject(x = 0.1013, y = 0.1069, z = 0.0238, roll = 2.519, pitch = 1.423, yaw = -2.371)
robot.move_pose(point)
point = PoseObject(x = 0.1304, y = 0.0083, z = 0.1527, roll = -1.871, pitch = 1.536, yaw = -1.180)
robot.move_pose(point)
point = PoseObject(x = 0.1106, y = -0.0934, z = 0.0275, roll = 2.046, pitch = 1.487, yaw = 2.006)
robot.move_pose(point)
point = PoseObject(x = 0.1106, y = -0.0934, z = 0.0275, roll = 2.046, pitch = 1.487, yaw = 2.006)
robot.move_pose(point)
point = PoseObject(x = 0.3013, y = -0.0837, z = 0.0313, roll = -2.337, pitch = 1.547, yaw = -2.451)
robot.move_pose(point)
point = PoseObject(x = 0.2314, y = 0.0297, z = 0.2052, roll = 1.423, pitch = 1.545, yaw = 1.860)
robot.move_pose(point)
point = PoseObject(x = 0.1027, y = 0.0072, z = 0.1624, roll = -0.114, pitch = 1.447, yaw = 0.243)
robot.move_pose(point)

robot.close_connection()