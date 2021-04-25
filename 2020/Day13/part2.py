from functools import reduce

def find_schedule(input):
    N = reduce(lambda x, y: x*y, map(lambda x: x[0], input))
    Ai = [a[0]-a[1] for a in input]
    Ni = [N//x for x in map(lambda x: x[0], input)]
    Yi = [pow(N, -1, n) for N, n in zip(Ni, map(lambda x: x[0], input))] # only for python >= 3.8
    return sum([a*n*y for a, n, y in zip(Ai, Ni, Yi)]) % N


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = [(int(i), index) for index, i in enumerate(input.splitlines()[1].split(',')) if i != 'x']
    print(find_schedule(input))