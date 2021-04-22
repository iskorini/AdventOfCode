from functools import reduce

def search_bus(start, bus):
    return reduce(lambda x, y: x*y, min([(b*((start//b)+1)-start, b) for b in bus]))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input=f.read()
    input = input.splitlines()
    start = int(input[0])
    bus = [int(b) for b in input[1].split(',') if b != 'x']
    print(search_bus(start, bus))
    