if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    groups = input.split('\n\n')
    unique_answers = 0
    for group in groups:
        counter = [False]*26
        for ans in group.replace('\n', ''):
            counter[ord(ans)-97] = True
        unique_answers += sum(counter)
    print(unique_answers)