FB_to_decimal = {}
LR_to_decimal = {}

FB_to_binary = {
    'B': 1,
    'F': 0
}

LR_to_binary = {
    'L': 0, 
    'R': 1
}

def create_fn(pow, dict):
    return lambda x: dict[x]*(2**pow)

def get_dec(value, pos, dict1, dict2):
    if pos in dict1:
        pass
    else:
        dict1[pos] = create_fn(pos, dict2)
    return dict1[pos](value) 

def get_res(input):
    res1 = sum([get_dec(x, i, FB_to_decimal, FB_to_binary) for i, x in enumerate(input[3:])])
    res2 = sum([get_dec(x, i, LR_to_decimal, LR_to_binary) for i, x in enumerate(input[0:3])])
    return res1 * 8 + res2

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    print(max([get_res(line[::-1]) for line in input.splitlines()]))