def navigate(commands, start_coordinates=[0, 0], waypoint_start_position = (-10, 1)):
    coordinates = start_coordinates
    waypoint_position = waypoint_start_position
    action = {
        'N': lambda c, v: (c[0], c[1]+v),
        'S': lambda c, v: (c[0], c[1]-v),
        'E': lambda c, v: (c[0]-v, c[1]),
        'W': lambda c, v: (c[0]+v, c[1]),
    }
    rotation = {
        0: lambda c, d: c,
        90: lambda c, d: (d*c[1], d*-1*c[0]),
        180: lambda c, d: (-1*c[0], -1*c[1]),
        270: lambda c, d: (d*-1*c[1], d*c[0])
    }
    change_direction = {
        'L': 1,
        'R': -1
    }
    for cmd in commands:
        c = cmd[0]
        arg = int(cmd[1:])
        if c in action.keys():
            waypoint_position = action[c](waypoint_position, arg)
        elif c in change_direction.keys():
            waypoint_position = rotation[arg](waypoint_position, change_direction[c])
        elif c in ['F']:
            coordinates[0] += arg*waypoint_position[0]
            coordinates[1] += arg*waypoint_position[1]
    return sum([abs(c) for c in coordinates])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    print(navigate(input))
        
    