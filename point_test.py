from pyniryo2 import *

def connect_and_calibrate():
    # try:
        r = NiryoRobot("192.168.6.50")
    # except Error as e:
        # robot = NiryoRobot("localhost")
        r.arm.calibrate_auto()
        r.tool.update_tool()
        return r


robot = connect_and_calibrate()
conveyor_id = robot.conveyor.set_conveyor()
#home = PoseObject(x=0.1402, y=0.0000, z=0.2033, roll=0.002, pitch=0.751, yaw=0.000)
home = PoseObject(x = 0.0800,  y = 0.3600, z = 0.0350, roll = 0.520,  pitch = 1.570, yaw = 0.657)
robot.arm.move_pose(home)

upper_source_points = []
upper_source_points.append(PoseObject(x = 0.0759, y = 0.3614, z = 0.1343, roll = 0.520, pitch = 1.544, yaw = 0.657))
upper_source_points.append(PoseObject(x = 0.0806, y = 0.3018, z = 0.1363, roll = -1.161, pitch = 1.537, yaw = -0.987))
upper_source_points.append(PoseObject(x = 0.0201, y = 0.2992, z = 0.1347, roll = -2.339, pitch = 1.526, yaw = -1.972))
upper_source_points.append(PoseObject(x = 0.0124, y = 0.3540, z = 0.1334, roll = 0.105, pitch = 1.519, yaw = 0.208))
upper_source_points.append(PoseObject(x = -0.0507, y = 0.3465, z = 0.1335, roll = -2.896, pitch = 1.564, yaw = -2.717))
upper_source_points.append(PoseObject(x = -0.0421, y = 0.2888, z = 0.1351, roll = 1.513, pitch = 1.546, yaw = 1.751))
upper_source_points.append(PoseObject(x = -0.1025, y = 0.2848, z = 0.1353, roll = 2.821, pitch = 1.530, yaw = -3.047))
upper_source_points.append(PoseObject(x = -0.1127, y = 0.3434, z = 0.1323, roll = -0.089, pitch = 1.543, yaw = 0.471))
upper_source_points.append(PoseObject(x = -0.1776, y = 0.3392, z = 0.1319, roll = -0.252, pitch = 1.537, yaw = 0.490))
upper_source_points.append(PoseObject(x = -0.1699, y = 0.2792, z = 0.1342, roll = -2.256, pitch = 1.499, yaw = -1.068))

i = 0
source_points = []

source_points.append(PoseObject(x = 0.0800,  y = 0.3600, z = 0.0350, roll = 0.520,  pitch = 1.570, yaw = 0.657))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = 0.0800,  y = 0.3000, z = 0.0350, roll = -1.161, pitch = 1.570, yaw = -0.987))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1

source_points.append(PoseObject(x = 0.0200,  y = 0.3000, z = 0.0350, roll = -2.339, pitch = 1.570, yaw = -1.972))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = 0.0200,  y = 0.3600, z = 0.0350, roll = 0.105,  pitch = 1.570, yaw = 0.208))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = -0.0400, y = 0.3600, z = 0.0350, roll = -2.896, pitch = 1.570, yaw = -2.717))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = -0.0400, y = 0.3000, z = 0.0350, roll = 1.513,  pitch = 1.570, yaw = 1.751))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = -0.1000, y = 0.3000, z = 0.0350, roll = 2.821,  pitch = 1.570, yaw = -3.047))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = -0.1000, y = 0.3600, z = 0.0350, roll = -0.089, pitch = 1.570, yaw = 0.471))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = -0.1600, y = 0.3600, z = 0.0350, roll = -0.252, pitch = 1.570, yaw = 0.490))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1
source_points.append(PoseObject(x = -0.1600, y = 0.3000, z = 0.0350, roll = -2.256, pitch = 1.570, yaw = -1.068))
robot.arm.move_pose(upper_source_points[i])
robot.arm.move_pose(source_points[i])
robot.arm.move_pose(upper_source_points[i])
i += 1


robot.arm.move_pose(home)
#robot.tool.release_with_tool()
#robot.conveyor.stop_conveyor(conveyor_id)

#robot.conveyor.unset_conveyor(conveyor_id)
robot.end()
