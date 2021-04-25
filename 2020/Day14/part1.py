def handle_mem(input):
    memory = {}
    actual_mask = None
    for line in input:
        if 'mask' in line:
            actual_mask = [(b, index) for index, b in enumerate(line[7:]) if b != 'X']
        elif 'mem' in line:
            data = list(format(int(line.split()[-1]), 'b').zfill(36))
            address = int(line.split()[0][4:-1])
            for m in actual_mask:
                data[m[1]] = m[0]
            memory[address] = int(''.join(data), 2)
    return sum([memory[k] for k in memory.keys()])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    print(handle_mem(input))
 