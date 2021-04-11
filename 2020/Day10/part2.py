def test_adpt(input):
    reachable = {0:1}
    for adapter in input:
        reachable[adapter] = reachable.get(adapter-1,0) + reachable.get(adapter-2,0) + reachable.get(adapter-3,0)
    return reachable[input[-1]]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    input = sorted([int(i) for i in input])
    print(test_adpt(input))