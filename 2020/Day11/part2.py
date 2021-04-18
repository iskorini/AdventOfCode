FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'

def get_occupied_seats(input):
    occupied_counter = 0
    changed = True
    new_disposition = [row.copy() for row in input]
    while changed:
        changed = False
        for x, row in enumerate(input):
            for y, seat in enumerate(row):
                adj = get_adj(input, (x, y))
                if seat == EMPTY and OCCUPIED not in adj:
                    new_disposition[x][y] = OCCUPIED
                    changed = True
                    occupied_counter += 1
                elif seat == OCCUPIED and adj.count(OCCUPIED)>=5:
                    new_disposition[x][y] = EMPTY
                    changed = True
                    occupied_counter -= 1
        input = new_disposition
        new_disposition = [row.copy() for row in input]
    return occupied_counter


def get_first_seat(input, start_position, condition, step_fn):
    def position_generator():
        position = step_fn(*start_position)
        while condition(*position):
            yield position
            position = step_fn(*position)
    pos_generator = position_generator()
    for position in pos_generator:
        if input[position[0]][position[1]] != FLOOR:
            return input[position[0]][position[1]]
    return FLOOR

    

def get_adj(input, position):
    adj = []
    #Vertical indexing on x, horizontal indexing on y
    #Down
    adj.append(get_first_seat(input, position, lambda a, b: a<len(input), lambda a, b: (a+1, b)))
    #Up
    adj.append(get_first_seat(input, position, lambda a, b: a>=0, lambda a, b: (a-1, b)))
    #Left
    adj.append(get_first_seat(input, position, lambda a, b: b>=0, lambda a, b: (a, b-1)))
    #Right
    adj.append(get_first_seat(input, position, lambda a, b: b<len(input[a]), lambda a, b: (a, b+1)))
    #Down Right
    adj.append(get_first_seat(input, position, lambda a, b: a<len(input) and b<len(input[a]), lambda a, b: (a+1, b+1)))
    #Down Left
    adj.append(get_first_seat(input, position, lambda a, b: a<len(input) and b>=0, lambda a, b: (a+1, b-1)))
    #Up Right
    adj.append(get_first_seat(input, position, lambda a, b: a>=0 and b<len(input[a]), lambda a, b: (a-1, b+1)))
    #Up Left
    adj.append(get_first_seat(input, position, lambda a, b: a>=0 and b>=0, lambda a, b: (a-1, b-1)))
    return adj

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = [list(row) for row in input.splitlines()]
    print(get_occupied_seats(input))