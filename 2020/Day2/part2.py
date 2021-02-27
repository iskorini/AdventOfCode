def check_psw(psw: str, letter, rng:str) -> bool:
    rng = [int(i) for i in rng.split('-')]
    return (bool(letter == psw[rng[0]-1]) ^ bool(letter == psw[rng[1]-1]))

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        input = f.read()
    input = input.split('\n')
    valid = 0
    for entry in input:
        rng, letter, psw = entry.split()
        valid += check_psw(psw, letter[0], rng)
    print(valid)
