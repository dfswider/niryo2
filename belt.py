from pyniryo2 import *

robot = NiryoRobot("192.168.6.50")
robot.arm.calibrate_auto()
robot.tool.update_tool()
conveyor_id = robot.conveyor.set_conveyor()

robot.conveyor.run_conveyor(conveyor_id, speed=50, direction=ConveyorDirection.FORWARD)
robot.wait(5)
robot.conveyor.stop_conveyor(conveyor_id)
robot.wait(3)
robot.conveyor.run_conveyor(conveyor_id, speed=50, direction=ConveyorDirection.BACKWARD)
robot.wait(5)
robot.conveyor.stop_conveyor(conveyor_id)

robot.conveyor.unset_conveyor(conveyor_id)
robot.end()
