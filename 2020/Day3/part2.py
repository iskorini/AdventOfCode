def check_trees(input, slope) -> int:
    trees = 0
    x = 0
    for y in range(0, len(input), slope[1]):
        trees += int(input[y][x] == '#')
        x = (x+slope[0])%len(input[y])
    return trees


if __name__ == '__main__':
    from functools import reduce

    with open('./input.txt', 'r') as f:
        input = f.read()
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    input = input.splitlines()
    print(reduce(lambda x, y: x*y, [check_trees(input, slope) for slope in slopes]))
