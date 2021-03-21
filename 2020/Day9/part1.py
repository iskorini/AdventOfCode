import numpy as np

def check(input, preamble_len=25):
    for i in range(preamble_len, len(input)):
        sums = []
        preamble = input[i-preamble_len:i]
        for j, n in enumerate(preamble):
            for k in preamble[j+1:]:
                sums.append(n+k)
        if input[i] not in sums:
            return input[i]

def check2(input, preamble_len=25):
    sums = np.zeros([len(input)]*2, dtype=int)
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            sums[j][i] = input[j]+input[i]
    i = preamble_len
    while input[i] in sums[i-preamble_len:i, i-preamble_len:i]:
        i+=1
    return input[i]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    input = [int(i) for i in input]
    print(check(input))
    print(check2(input))