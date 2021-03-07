TERMINAL = 'noother'
COLOR = 'shinygold'

def generate_dict(input):
    d = {}
    for line in input:
        line = line.split('contain')
        content = line[1].split(',')
        content = list(map(lambda x: ''.join(
            filter(lambda x: not x.isdigit(), x)).replace(' ', ''), content)
            )
        d[line[0].replace(' ', '')] = content
    return d

def porca_madonna(d, key):
    try:
        for bag in d[key]:
            porca_madonna(d, bag)
        d.pop(key, None)
    except KeyError:
        pass

def gesu_cretino(key, d):
    try:
        bag_content = d[key]
        if COLOR in bag_content:
            return 1
        elif TERMINAL in bag_content: 
            d.pop(key, None)
            return 0
        i = len(bag_content)
        for bag in bag_content:
            if gesu_cretino(bag, d) == 0:
                i = i-1
        if i <= 0:
            d.pop(key, None)
            return 0
    except KeyError:
        return 0

def dio_rotto(d):
    try:
        bags = list(d.keys())
        for bag in bags:
            if gesu_cretino(bag, d) == 0:
                d.pop(bag, None)
    except KeyError:
        pass


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = input.replace('bags', 'bag').replace('bag', '').replace('.', '')
    input = input.splitlines()
    d = generate_dict(input)
    porca_madonna(d, COLOR)
    dio_rotto(d)
    print(len(d.keys()))
