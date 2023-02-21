from pyniryo import *

robot = NiryoRobot("192.168.6.50")
#client = robot.client
#robot.arm.calibrate_auto()
#robot.tool.update_tool()

#joints =

status = robot.get_hardware_status()
print(status)
dio = robot.get_digital_io_state()
print(dio)
aio = robot.get_analog_io_state()
print(aio)

#robot.end()
robot.close_connection()
