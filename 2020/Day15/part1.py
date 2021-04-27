from os import lseek


def game(input, turns=2021):
    memory = {}
    for index, i in enumerate(input[:-1]):
        memory[i] = index
    last_spoken = input[-1]
    for i in range(len(input), turns):
        if memory.get(last_spoken, None) is None:
            to_spoke = 0
        else:
            to_spoke = i-1-memory[last_spoken]
        memory[last_spoken] = i-1
        last_spoken = to_spoke
    return last_spoken

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read().split(',')
    input = [int(i) for i in input]
    print(game(input, 2020))
    