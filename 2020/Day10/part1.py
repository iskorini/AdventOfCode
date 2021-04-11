def test_adapters(input):
    input = sorted(input)
    diffs = {
        1: 0,
        2: 0, 
        3: 1
    }
    actual_adapter = 0
    for adapter in input:
        diffs[adapter-actual_adapter] += 1
        actual_adapter = adapter
    return diffs[1]*diffs[3]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.splitlines()
    input = [int(i) for i in input]
    print(test_adapters(input))