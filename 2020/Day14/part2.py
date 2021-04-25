from itertools import product

def handle_mem(input):
    memory = {}
    actual_mask = None
    for line in input:
        if 'mask' in line:
            actual_mask = line[7:]
        elif 'mem' in line:
            data = int(line.split()[-1])
            address = list(format(int(line.split()[0][4:-1]), 'b').zfill(36))
            mask = [(v, index) for index, v in enumerate(actual_mask) if v != '0']
            for m in mask:
                address[m[1]] = m[0]
            for p in product('01', repeat=actual_mask.count('X')):
                tmp_address = ''.join(address)
                for b in p:
                    tmp_address = tmp_address.replace('X', b, 1)
                memory[int(''.join(tmp_address), 2)] = data
    return sum([memory[k] for k in memory.keys()])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    print(handle_mem(input))
 