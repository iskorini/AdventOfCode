import numpy as np

to_binary = {
    'B': 1,
    'F': 0,
    'L': 0,
    'R': 1
}

def get_res(input):
    row = sum([to_binary[x]*(2**i) for i, x in enumerate(input[3:])])
    column = sum([to_binary[x]*(2**i) for i, x in enumerate(input[0:3])])
    return row * 8 + column

def find_seat(seat_list):
    for i, j in zip(range(0, len(seat_list)-1), range(1, len(seat_list))):
        yield seat_list[i]+1, (seat_list[i]+1 != seat_list[j])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    ordered_decimal_input = sorted([get_res(line[::-1]) for line in input.splitlines()])
    datagen = find_seat(ordered_decimal_input)
    seat, missing = next(datagen)
    while not missing:
        seat, missing = next(datagen)
    print(seat)