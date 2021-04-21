def navigate(commands, start_direction=90):
    direction = start_direction
    coordinates = (0,0) 
    action = {
        'N': lambda c, v: (c[0], c[1]+v),
        'S': lambda c, v: (c[0], c[1]-v),
        'E': lambda c, v: (c[0]-v, c[1]),
        'W': lambda c, v: (c[0]+v, c[1]),
    }
    directions_to_action = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W' 
    }
    change_direction = {
        'L': lambda d, v: d-v,
        'R': lambda d, v: d+v
    }
    #Action F means to move forward by the given value in the direction the ship is currently facing.
    for cmd in commands:
        c = cmd[0]
        arg = int(cmd[1:])
        if c in action.keys():
            coordinates = action[c](coordinates, arg)
        elif c in change_direction.keys():
            direction = change_direction[c](direction, arg) % 360
        elif c in ['F']:
            coordinates = action[directions_to_action[direction]](coordinates, arg)
    return sum([abs(c) for c in coordinates])




if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    print(navigate(input))
        
    