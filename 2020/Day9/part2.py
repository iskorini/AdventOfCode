def check(input, preamble_len=25):
    for i in range(preamble_len, len(input)):
        sums = []
        preamble = input[i-preamble_len:i]
        for j, n in enumerate(preamble):
            for k in preamble[j+1:]:
                sums.append(n+k)
        if input[i] not in sums:
            return input[i]

def find_weakness(input, invalid_number):
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            s = sum(input[i:j])
            if s == invalid_number:
                l = sorted(input[i:j])
                return l[0]+l[-1]
            elif s > invalid_number:
                continue

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    input = [int(i) for i in input]
    invalid_number = check(input)
    print(find_weakness(input, invalid_number))