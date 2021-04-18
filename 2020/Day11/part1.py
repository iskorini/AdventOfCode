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
                elif seat == OCCUPIED and adj.count(OCCUPIED)>=4:
                    new_disposition[x][y] = EMPTY
                    changed = True
                    occupied_counter -= 1
        input = new_disposition
        new_disposition = [row.copy() for row in input]
    return occupied_counter

def get_adj(input, position):
    adj = [FLOOR]*8 
    x, y = position
    up_ok = x-1 >= 0
    down_ok = x+1 < len(input)
    right_ok = y+1 < len(input[x])
    left_ok = y-1 >= 0
    adj[0] = input[x-1][y] if up_ok else FLOOR
    adj[1] = input[x+1][y] if down_ok else FLOOR
    adj[2] = input[x][y-1] if left_ok else FLOOR
    adj[3] = input[x][y+1] if right_ok else FLOOR
    adj[4] = input[x-1][y-1] if (up_ok and left_ok) else FLOOR
    adj[5] = input[x-1][y+1] if (up_ok and right_ok) else FLOOR
    adj[6] = input[x+1][y-1] if (down_ok and left_ok) else FLOOR
    adj[7] = input[x+1][y+1] if (down_ok and right_ok) else FLOOR
    return adj

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = [list(row) for row in input.splitlines()]
    print(get_occupied_seats(input))