"""box_obstacle1 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor, Robot
import optparse
import math

idx_dict = {"x":0, "y":1, "z":2}

# create the Supervisor instance.
supervisor = Supervisor()
robot_node = supervisor.getSelf()
trans_field = robot_node.getField("translation")
print(trans_field)


# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())
print(f"Timestep: {timestep}")

# get the starting position of the box
start_pos = trans_field.getSFVec3f()

# compute the distance to be travelled
goal = start_pos
goal[1] = -start_pos[1]
distance = 2*abs(start_pos[1])

# the speed can be set from the user
opt_parser = optparse.OptionParser()
opt_parser.add_option("--speed", type=float, default=0.2, help="Specify the box moving speed in [m/s]")
opt_parser.add_option("--direction", type=str, default="+y", help="Specify direction in the global reference frame along which the box has to move: +/- x,y or z")
options, args = opt_parser.parse_args()
target_speed = options.speed

# process the direction
direction = list(options.direction)
idx_speed = 0

if direction[0] == "+":
    versus = 1
else:
    versus = -1

for key in idx_dict:
    if key==direction[1]: idx_speed = idx_dict[key]


# time for one forwart travel
t = int(distance/target_speed)
print(t)


speed = robot_node.getVelocity()

while supervisor.step(timestep) != -1:
    speed[idx_speed] = target_speed*versus
    robot_node.setVelocity(speed)
    supervisor.step(t*1000)

    speed[idx_speed] = -target_speed*versus
    robot_node.setVelocity(speed)
    supervisor.step(t*1000)



