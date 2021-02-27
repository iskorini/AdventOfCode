def get_combinations(input, n, prefix=[]):
    if n == 1:
        for i in input:
            yield prefix+[i]    
    else:
        for i in range(0, len(input)-n+1):
            yield from get_combinations(input[i+1:], n-1, prefix+[input[i]])
    

if __name__ == '__main__':
    from functools import reduce

    with open('input.txt', 'r') as f:
        input_file = f.read().split('\n')
    input_file = [int(i) for i in input_file]
    generator = get_combinations(input_file, 3)
    cmb = next(generator)
    while sum(cmb) != 2020:
        cmb = next(generator)
    print(cmb)
    print(reduce(lambda x, y: x*y, cmb))
