from pyniryo2 import *
from roslibpy.core import RosTimeoutError

source_points = []
upper_source_points = []
destination_points = []
upper_destination_points = []
v = 15

source_points.append(PoseObject(x = 0.0543, y = 0.3835, z = 0.2364, roll = 3.035, pitch = -1.395, yaw = 1.180))
source_points.append(PoseObject(x = 0.0518, y = 0.2812, z = 0.3476, roll = -0.327, pitch = -1.427, yaw = -1.775))
source_points.append(PoseObject(x = -0.0184, y = 0.3723, z = 0.2591, roll = 2.363, pitch = -1.485, yaw = 2.280))
source_points.append(PoseObject(x = -0.0089, y = 0.2765, z = 0.3513, roll = -0.066, pitch = -1.330, yaw = -1.660))
source_points.append(PoseObject(x = -0.0791, y = 0.3614, z = 0.2620, roll = -2.540, pitch = -1.521, yaw = 1.260))
source_points.append(PoseObject(x = -0.0605, y = 0.2587, z = 0.3574, roll = -0.025, pitch = -1.283, yaw = -1.224))
source_points.append(PoseObject(x = -0.1473, y = 0.3572, z = 0.2337, roll = -2.742, pitch = -1.440, yaw = 1.806))
source_points.append(PoseObject(x = -0.1154, y = 0.2600, z = 0.3452, roll = 0.017, pitch = -1.341, yaw = -0.900))
source_points.append(PoseObject(x = -0.2149, y = 0.3499, z = 0.1810, roll = -2.745, pitch = -1.308, yaw = 2.102))
source_points.append(PoseObject(x = -0.1794, y = 0.2701, z = 0.3148, roll = -0.389, pitch = -1.422, yaw = -0.169))


upper_source_points.append(PoseObject(x = 0.0543, y = 0.3835, z = 0.2364, roll = 3.035, pitch = -1.395, yaw = 1.180))
upper_source_points.append(PoseObject(x = 0.0518, y = 0.2812, z = 0.3476, roll = -0.327, pitch = -1.427, yaw = -1.775))
upper_source_points.append(PoseObject(x = -0.0184, y = 0.3723, z = 0.2591, roll = 2.363, pitch = -1.485, yaw = 2.280))
upper_source_points.append(PoseObject(x = -0.0089, y = 0.2765, z = 0.3513, roll = -0.066, pitch = -1.330, yaw = -1.660))
upper_source_points.append(PoseObject(x = -0.0791, y = 0.3614, z = 0.2620, roll = -2.540, pitch = -1.521, yaw = 1.260))
upper_source_points.append(PoseObject(x = -0.0605, y = 0.2587, z = 0.3574, roll = -0.025, pitch = -1.283, yaw = -1.224))
upper_source_points.append(PoseObject(x = -0.1473, y = 0.3572, z = 0.2337, roll = -2.742, pitch = -1.440, yaw = 1.806))
upper_source_points.append(PoseObject(x = -0.1154, y = 0.2600, z = 0.3452, roll = 0.017, pitch = -1.341, yaw = -0.900))
upper_source_points.append(PoseObject(x = -0.2149, y = 0.3499, z = 0.1810, roll = -2.745, pitch = -1.308, yaw = 2.102))
upper_source_points.append(PoseObject(x = -0.1794, y = 0.2701, z = 0.3148, roll = -0.389, pitch = -1.422, yaw = -0.169))





# p1_before_pick = PoseObject(x=0.0950, y=0.2824, z=0.1899, roll=1.607, pitch=1.439, yaw=-3.061)
# p2_release_to_conveyor = PoseObject(x=0.2054, y=0.2859, z=0.1100, roll = 2.603, pitch=1.518, yaw=2.559)
# p3_after_release_to_conveyor = PoseObject(x=0.2828, y=0.0599, z=0.2115, roll=-2.852, pitch=1.443, yaw=-2.847)
# p4_before_pick_from_conveyor = PoseObject(x=0.2243, y=-0.3150, z=0.1850, roll=-2.487, pitch=1.492, yaw = -2.406)
# p5_after_pick_from_conveyor = PoseObject(x=0.2124, y=-0.3206, z=0.0922, roll=-2.255, pitch=1.527, yaw=-2.265)
# p6_before_release = PoseObject(x=0.1030, y=-0.3072, z=0.1814, roll=-2.371, pitch=1.550, yaw=2.312)

#after_pick
after_pick = PoseObject(x=0.0942, y=0.2502, z=0.3917, roll=-0.135, pitch=-0.902, yaw=-1.806)
#before_release
before_release = PoseObject(x=0.2037, y=0.3037, z=0.3081, roll=0.540, pitch=-1.299, yaw=-1.872)
#release_point
release_point = PoseObject(x=0.2085, y=0.3115, z=0.2875, roll=0.456, pitch=-1.374, yaw=-1.807)
#before_pick_from_conveyor
before_pick_from_conveyor = PoseObject(x = 0.2596, y = -0.2663, z = 0.3008, roll = -1.320, pitch = -1.400, yaw = 2.775)
#pick_from_conveyor
pick_from_conveyor = PoseObject(x = 0.2684, y = -0.2687, z = 0.2807, roll = -1.228, pitch = -1.478, yaw = 2.653)
#after_pick_from_conveyor
after_pick_from_conveyor = PoseObject(x = 0.1525, y = -0.2255, z = 0.3926, roll = -0.363, pitch = -0.926, yaw = 2.122)


destination_points.append(PoseObject(x = 0.1120, y = -0.2512, z = 0.3571, roll = 0.376, pitch = -1.368, yaw = 1.884))
destination_points.append(PoseObject(x = 0.1326, y = -0.3554, z = 0.2568, roll = -3.057, pitch = -1.426, yaw = -1.181))
destination_points.append(PoseObject(x = 0.0553, y = -0.2436, z = 0.3701, roll = 0.175, pitch = -1.302, yaw = 1.699))
destination_points.append(PoseObject(x = 0.0643, y = -0.3527, z = 0.2882, roll = -2.329, pitch = -1.524, yaw = -2.109))
destination_points.append(PoseObject(x = 0.0015, y = -0.2467, z = 0.3727, roll = -0.282, pitch = -1.256, yaw = 1.709))
destination_points.append(PoseObject(x = 0.0065, y = -0.3551, z = 0.2920, roll = 2.683, pitch = -1.544, yaw = -1.238))
destination_points.append(PoseObject(x = -0.0510, y = -0.2575, z = 0.3655, roll = -0.454, pitch = -1.326, yaw = 1.448))
destination_points.append(PoseObject(x = -0.0629, y = -0.3722, z = 0.2583, roll = 3.079, pitch = -1.447, yaw = -2.069))
destination_points.append(PoseObject(x = -0.1160, y = -0.2867, z = 0.3352, roll = -0.591, pitch = -1.423, yaw = 1.201))
destination_points.append(PoseObject(x = -0.1248, y = -0.3823, z = 0.2106, roll = 2.564, pitch = -1.373, yaw = -1.867))

upper_destination_points.append(PoseObject(x = 0.1120, y = -0.2512, z = 0.3571, roll = 0.376, pitch = -1.368, yaw = 1.884))
upper_destination_points.append(PoseObject(x = 0.1326, y = -0.3554, z = 0.2568, roll = -3.057, pitch = -1.426, yaw = -1.181))
upper_destination_points.append(PoseObject(x = 0.0553, y = -0.2436, z = 0.3701, roll = 0.175, pitch = -1.302, yaw = 1.699))
upper_destination_points.append(PoseObject(x = 0.0643, y = -0.3527, z = 0.2882, roll = -2.329, pitch = -1.524, yaw = -2.109))
upper_destination_points.append(PoseObject(x = 0.0015, y = -0.2467, z = 0.3727, roll = -0.282, pitch = -1.256, yaw = 1.709))
upper_destination_points.append(PoseObject(x = 0.0065, y = -0.3551, z = 0.2920, roll = 2.683, pitch = -1.544, yaw = -1.238))
upper_destination_points.append(PoseObject(x = -0.0510, y = -0.2575, z = 0.3655, roll = -0.454, pitch = -1.326, yaw = 1.448))
upper_destination_points.append(PoseObject(x = -0.0629, y = -0.3722, z = 0.2583, roll = 3.079, pitch = -1.447, yaw = -2.069))
upper_destination_points.append(PoseObject(x = -0.1160, y = -0.2867, z = 0.3352, roll = -0.591, pitch = -1.423, yaw = 1.201))
upper_destination_points.append(PoseObject(x = -0.1248, y = -0.3823, z = 0.2106, roll = 2.564, pitch = -1.373, yaw = -1.867))

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

home_to_source = PoseObject(x = 0.0601, y = 0.3225, z = 0.1066, roll = 0.626, pitch = 1.528, yaw = 2.140)
robot.arm.move_pose(home_to_source)

conveyor_id = robot.conveyor.set_conveyor()
# robot.conveyor.run_conveyor(conveyor_id, speed=v, direction=ConveyorDirection.FORWARD)

for i in range(0, 10):
    robot.arm.move_pose(after_pick)
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
