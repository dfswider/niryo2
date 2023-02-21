from pyniryo import *

robot = NiryoRobot("192.168.6.50")

robot.calibrate_auto()
robot.update_tool()

status = robot.get_hardware_status()
print(status)
dio = robot.get_digital_io_state()
print(dio)
aio = robot.get_analog_io_state()
print(aio)

#robot.release_with_tool()
#robot.move.pose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

robot.move.pose(0.2, -0.1, 0.25, 0.0, 1.57, 0.0)
robot.grasp_with_tool()

robot.move.pose(0.2, 0.1, 0.25, 0.0, 1.57, 0.0)
robot.release_with_tool()

robot.close_connection()
