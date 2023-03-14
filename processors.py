from pyniryo2 import *
from roslibpy.core import RosTimeoutError

source_points = []
upper_source_points = []
destination_points = []
upper_destination_points = []
v = 15

source_points.append(PoseObject(x=0.0800,  y=0.3100, z=0.0350, roll=3.135,  pitch=1.450, yaw=-1.543))
source_points.append(PoseObject(x=0.0800,  y=0.2500, z=0.0350, roll=2.492,  pitch=1.467, yaw=-2.109))
source_points.append(PoseObject(x=0.0150,  y=0.3100, z=0.0350, roll=3.022,  pitch=1.473, yaw=-1.701))
source_points.append(PoseObject(x=0.0150,  y=0.2500, z=0.0350, roll=2.931,  pitch=1.432, yaw=-1.711))
source_points.append(PoseObject(x=-0.0500, y=0.3100, z=0.0350, roll=-2.748, pitch=1.509, yaw=-1.175))
source_points.append(PoseObject(x=-0.0500, y=0.2500, z=0.0350, roll=2.965,  pitch=1.462, yaw=-1.696))
source_points.append(PoseObject(x=-0.1000, y=0.3100, z=0.0350, roll=2.855,  pitch=1.544, yaw=-1.768))
source_points.append(PoseObject(x=-0.1000, y=0.2500, z=0.0350, roll=-2.766, pitch=1.504, yaw=-1.122))
source_points.append(PoseObject(x=-0.1650, y=0.3100, z=0.0350, roll=-1.925, pitch=1.501, yaw=-0.276))
source_points.append(PoseObject(x=-0.1650, y=0.2500, z=0.0350, roll=-3.119, pitch=1.508, yaw=-1.448))


upper_source_points.append(PoseObject(x=0.0800,  y=0.2971, z=0.1, roll=3.135,  pitch=1.450, yaw=-1.543))
upper_source_points.append(PoseObject(x=0.0800,  y=0.2344, z=0.1, roll=2.492,  pitch=1.467, yaw=-2.109))
upper_source_points.append(PoseObject(x=0.0150,  y=0.2919, z=0.1, roll=3.022,  pitch=1.473, yaw=-1.701))
upper_source_points.append(PoseObject(x=0.0150,  y=0.2318, z=0.1, roll=2.931,  pitch=1.432, yaw=-1.711))
upper_source_points.append(PoseObject(x=-0.0500, y=0.2874, z=0.1, roll=-2.748, pitch=1.509, yaw=-1.175))
upper_source_points.append(PoseObject(x=-0.0500, y=0.2279, z=0.1, roll=2.965,  pitch=1.462, yaw=-1.696))
upper_source_points.append(PoseObject(x=-0.1000, y=0.2846, z=0.1, roll=2.855,  pitch=1.544, yaw=-1.768))
upper_source_points.append(PoseObject(x=-0.1000, y=0.2218, z=0.1, roll=-2.766, pitch=1.504, yaw=-1.122))
upper_source_points.append(PoseObject(x=-0.1650, y=0.2795, z=0.1, roll=-1.925, pitch=1.501, yaw=-0.276))
upper_source_points.append(PoseObject(x=-0.1650, y=0.2198, z=0.1, roll=-3.119, pitch=1.508, yaw=-1.448))



p1_before_pick = PoseObject(x=0.0950, y=0.2824, z=0.1899, roll=1.607, pitch=1.439, yaw=-3.061)
p2_release_to_conveyor = PoseObject(x=0.2054, y=0.2859, z=0.1100, roll = 2.603, pitch=1.518, yaw=2.559)
p3_after_release_to_conveyor = PoseObject(x=0.2828, y=0.0599, z=0.2115, roll=-2.852, pitch=1.443, yaw=-2.847)
p4_before_pick_from_conveyor = PoseObject(x=0.2243, y=-0.3150, z=0.1850, roll=-2.487, pitch=1.492, yaw = -2.406)
p5_after_pick_from_conveyor = PoseObject(x=0.2124, y=-0.3206, z=0.0922, roll=-2.255, pitch=1.527, yaw=-2.265)
p6_before_release = PoseObject(x=0.1030, y=-0.3072, z=0.1814, roll=-2.371, pitch=1.550, yaw=2.312)

destination_points.append(PoseObject(x=0.0879,  y=-0.2679, z=0.0384, roll=1.364,  pitch=1.566, yaw=-0.237))
destination_points.append(PoseObject(x=0.0859,  y=-0.3257, z=0.0348, roll=0.415,  pitch=1.535, yaw=-1.204))
destination_points.append(PoseObject(x=0.0327,  y=-0.2676, z=0.0417, roll=-2.761, pitch=1.525, yaw=1.899))
destination_points.append(PoseObject(x=0.0271,  y=-0.3275, z=0.0400, roll=-1.146, pitch=1.554, yaw=-2.743))
destination_points.append(PoseObject(x=-0.0322, y=-0.2655, z=0.0406, roll=-2.988, pitch=1.517, yaw=1.670))
destination_points.append(PoseObject(x=-0.0337, y=-0.3225, z=0.0379, roll=0.043,  pitch=1.529, yaw=-1.492))
destination_points.append(PoseObject(x=-0.0962, y=-0.2640, z=0.0385, roll=1.985,  pitch=1.515, yaw=0.362))
destination_points.append(PoseObject(x=-0.0973, y=-0.3226, z=0.0379, roll=1.378,  pitch=1.501, yaw=-0.234))
destination_points.append(PoseObject(x=-0.1590, y=-0.2586, z=0.0379, roll=1.513,  pitch=1.502, yaw=-0.141))
destination_points.append(PoseObject(x=-0.1647, y=-0.3254, z=0.0375, roll=2.650,  pitch=1.473, yaw=1.112))

upper_destination_points.append(PoseObject(x=0.0879,  y=-0.2679, z=0.1, roll=1.364,  pitch=1.566, yaw=-0.237))
upper_destination_points.append(PoseObject(x=0.0859,  y=-0.3257, z=0.1, roll=0.415,  pitch=1.535, yaw=-1.204))
upper_destination_points.append(PoseObject(x=0.0327,  y=-0.2676, z=0.1, roll=-2.761, pitch=1.525, yaw=1.899))
upper_destination_points.append(PoseObject(x=0.0271,  y=-0.3275, z=0.1, roll=-1.146, pitch=1.554, yaw=-2.743))
upper_destination_points.append(PoseObject(x=-0.0322, y=-0.2655, z=0.1, roll=-2.988, pitch=1.517, yaw=1.670))
upper_destination_points.append(PoseObject(x=-0.0337, y=-0.3225, z=0.1, roll=0.043,  pitch=1.529, yaw=-1.492))
upper_destination_points.append(PoseObject(x=-0.0962, y=-0.2640, z=0.1, roll=1.985,  pitch=1.515, yaw=0.362))
upper_destination_points.append(PoseObject(x=-0.0973, y=-0.3226, z=0.1, roll=1.378,  pitch=1.501, yaw=-0.234))
upper_destination_points.append(PoseObject(x=-0.1590, y=-0.2586, z=0.1, roll=1.513,  pitch=1.502, yaw=-0.141))
upper_destination_points.append(PoseObject(x=-0.1647, y=-0.3254, z=0.1, roll=2.650,  pitch=1.473, yaw=1.112))

def connect_and_calibrate():
    try:
        r = NiryoRobot("192.168.6.50")
        #robot = NiryoRobot("localhost")
        r.arm.calibrate_auto()
        r.tool.update_tool()
    except RosTimeoutError as e:
        r = None
    finally:
        return r


robot = connect_and_calibrate()


home = PoseObject(x=0.1402, y=0.0000, z=0.2033, roll=0.002, pitch=0.751, yaw=0.000)
try:
    robot.arm.move_pose(home)
except RosTimeoutError as e:
    print(e)


conveyor_id = robot.conveyor.set_conveyor()
# robot.conveyor.run_conveyor(conveyor_id, speed=v, direction=ConveyorDirection.FORWARD)

for i in range(0, 10):
    robot.arm.move_pose(p1_before_pick)
    robot.arm.move_pose(upper_source_points[i])
    robot.arm.move_pose(source_points[i])
    robot.tool.grasp_with_tool()
    robot.arm.move_pose(upper_source_points[i])
    robot.arm.move_pose(p1_before_pick)
    robot.arm.move_pose(p2_release_to_conveyor)
    robot.tool.release_with_tool()
    robot.arm.move_pose(p1_before_pick)
    robot.conveyor.run_conveyor(conveyor_id, speed=v, direction=ConveyorDirection.FORWARD)
    robot.wait(4.5)
    robot.conveyor.stop_conveyor(conveyor_id)
    # robot.arm.move_pose(p1_before_pick)

robot.arm.move_pose(p3_after_release_to_conveyor)


for i in range(0, 10):
    robot.conveyor.stop_conveyor(conveyor_id)
    robot.arm.move_pose(p4_before_pick_from_conveyor)
    # pick it!!!
    robot.arm.move_pose(p5_after_pick_from_conveyor)
    robot.conveyor.run_conveyor(conveyor_id, speed=v, direction=ConveyorDirection.FORWARD)
    robot.arm.move_pose(p6_before_release)
    robot.arm.move_pose(upper_destination_points[i])
    robot.arm.move_pose(destination_points[i])
    # release to box
    robot.arm.move_pose(upper_destination_points[i])
    robot.arm.move_pose(p6_before_release)

robot.arm.move_pose(home)

robot.conveyor.stop_conveyor(conveyor_id)
robot.conveyor.unset_conveyor(conveyor_id)
robot.end()
