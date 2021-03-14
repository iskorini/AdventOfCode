def execute_boot(input):
    ptr = 0
    acc = 0
    counter = {} 
    while counter.get(ptr, 0) < 1:
        istr = input[ptr].split(' ')
        counter[ptr] = 1 + counter.get(ptr, 0)
        if istr[0] == 'nop':
            ptr += 1
        elif istr[0] == 'jmp':
            ptr += int(istr[1])
        elif istr[0] == 'acc':
            ptr += 1
            acc += int(istr[1])
    return acc 

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    acc = execute_boot(input)
    print(acc)
    