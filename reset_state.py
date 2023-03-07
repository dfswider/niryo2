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
home = PoseObject(x=0.1402, y=0.0000, z=0.2033, roll=0.002, pitch=0.751, yaw=0.000)

robot.arm.move_pose(home)
robot.tool.release_with_tool()
robot.conveyor.stop_conveyor(conveyor_id)

robot.conveyor.unset_conveyor(conveyor_id)
robot.end()

