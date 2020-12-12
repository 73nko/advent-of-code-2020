
import math


def get_instructions(filename):
    with open(filename) as input_file:
        local_list = input_file.readlines()
        return_list = [(item.strip()) for item in local_list]
        return return_list


def get_ship_position(instructions, verbose=False):
    heading = 0
    east = 0
    north = 0
    for line in instructions:
        cmd = line[0]
        dist = int(line[1:])
        if (cmd == 'F'):
            if (heading == 0):
                cmd = 'E'
            elif (heading == 90):
                cmd = 'N'
            elif (heading == 180):
                cmd = 'W'
            elif (heading == 270):
                cmd = 'S'
            else:
                north += math.sin(heading/180*math.pi)
                east += math.cos(heading/180*math.pi)
        if (cmd == 'N'):
            north += dist
        if (cmd == 'S'):
            north -= dist
        if (cmd == 'E'):
            east += dist
        if (cmd == 'W'):
            east -= dist
        if (cmd == 'L'):
            heading = (heading + dist) % 360
        if (cmd == 'R'):
            heading = (heading - dist) % 360
        if (verbose):
            print(cmd, dist, " -> ", east, north, heading)
    return (east, north, heading)


def rotate_waypoint(waypoint, angle):
    rot_matrices = {
        90: [(0, -1), (1, 0)],
        180: [(-1, 0), (0, -1)],
        270: [(0, 1), (-1, 0)]
    }
    rot = rot_matrices[angle]
    new_east = rot[0][0]*waypoint[0] + rot[0][1]*waypoint[1]
    new_north = rot[1][0]*waypoint[0] + rot[1][1]*waypoint[1]
    return [new_east, new_north]


def navigate2(instruction_list, verbose=False):
    ship_position = [0, 0]
    waypoint = [10, 1]
    for line in instruction_list:
        cmd = line[0]
        dist = int(line[1:])
        if (cmd == 'E'):
            waypoint[0] += dist
        if (cmd == 'W'):
            waypoint[0] -= dist
        if (cmd == 'N'):
            waypoint[1] += dist
        if (cmd == 'S'):
            waypoint[1] -= dist
        if (cmd == 'L'):
            waypoint = rotate_waypoint(waypoint, dist % 360)
        if (cmd == 'R'):
            waypoint = rotate_waypoint(waypoint, -dist % 360)
        if (cmd == 'F'):
            ship_position[0] += dist*waypoint[0]
            ship_position[1] += dist*waypoint[1]
        if (verbose):
            print(cmd, dist, " -> ", ship_position, waypoint)
    return ship_position


instructions = get_instructions("./day-12/instructions.txt")
e, n, h = get_ship_position(instructions)
star1 = abs(n) + abs(e)
print(f"ship position: {star1}")

pos = navigate2(instructions)
star2 = abs(pos[0]) + abs(pos[1])
print(f"Ship position 2: {star2}")
