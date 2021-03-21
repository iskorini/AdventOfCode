def execute_boot(input):
    ptr = 0
    acc = 0
    iteration = 0
    counter = {} 
    while ptr < len(input):
        istr = input[ptr].split(' ')
        counter[ptr] = 1 + counter.get(ptr, 0)
        if counter[ptr] > 1:
            return None
        acc, ptr = handle_istruction(istr, acc, ptr)
    return acc 

def handle_istruction(istr, acc, ptr):
    if istr[0] == 'nop':
        ptr += 1
    elif istr[0] == 'jmp':
        ptr += int(istr[1])
    elif istr[0] == 'acc':
        ptr += 1
        acc += int(istr[1])
    return acc, ptr
    
def generate_boot_sequence(original_input):
    swap = {
        'jmp': 'nop',
        'nop': 'jmp'
    }
    for i, instruction in enumerate(original_input):
        instruction = instruction.split()
        if instruction[0] == 'jmp' or instruction[0] == 'nop':
            yield original_input[:i]+[' '.join([swap[instruction[0]], instruction[1]])]+original_input[i+1:]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    original_input = input.splitlines()
    input_generator = generate_boot_sequence(original_input)
    acc = execute_boot(next(input_generator))
    while not acc:
        acc = execute_boot(next(input_generator))
    print(acc)

