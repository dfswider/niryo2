from pyniryo2 import *

# -- Setting variables
sensor_pin_id = PinID.GPIO_2B

catch_nb = 5

# The pick pose
pick_pose = PoseObject(
    x=0.25, y=0., z=0.15,
    roll=-0., pitch=1.57, yaw=0.0,
)
# The Place pose
place_pose = PoseObject(
    x=0., y=-0.25, z=0.1,
    roll=0., pitch=1.57, yaw=-1.57)

# -- MAIN PROGRAM

# Connecting to robot
robot = NiryoRobot("192.168.6.50")

# Activating connexion with conveyor
conveyor_id = robot.conveyor.set_conveyor()

for i in range(catch_nb):
    robot.conveyor.run_conveyor(conveyor_id)
    while robot.io.digital_read(sensor_pin_id) == PinState.LOW:
        robot.wait(0.1)

    # Stopping robot motor
    robot.conveyor.stop_conveyor(conveyor_id)
    # Making a pick & place
    robot.pick_place.pick_and_place(pick_pose, place_pose)

# Deactivating connexion with conveyor
robot.conveyor.unset_conveyor(conveyor_id)