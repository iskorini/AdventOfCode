import re

TERMINAL = 'no other'
COLOR = 'shiny gold'
digits = re.compile(r'^\d{1,}')
non_digits = re.compile(r'\D{1,}')

def parse_bags(input):
    d = {}
    for line in input:
        line = line.split('contain')
        content = line[1].split(',')
        content = list(map(lambda x: x[1:-1], content))
        if content[0] != TERMINAL:
            content = list(map(
                lambda x: (int(digits.match(x).group()), non_digits.findall(x)[0][1:])
                , content))
        else:
            content = [(0, TERMINAL)]
        d[line[0][:-2]] = content
    return d

def bag_counter(bags, bag_color):
    if bags[bag_color][0][1] == TERMINAL:
        return bags[bag_color][0][0]
    counter = 0
    for bag in bags[bag_color]:
        tmp = bag_counter(bags, bag[1])
        counter += bag[0] + bag[0]*tmp
    return counter

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.replace('bags', 'bag').replace('bag', '').replace('.', '')
    input = input.splitlines()
    bags = parse_bags(input)
    counter = bag_counter(bags, COLOR)
    print(counter)