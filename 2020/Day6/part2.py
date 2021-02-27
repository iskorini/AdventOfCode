if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    groups = input.split('\n\n')
    unique_answers = 0
    for group in groups:
        persons = group.splitlines()
        group_counter = [True] * 26
        for person in group.splitlines():
            person_counter = [False] * 26
            for ans in person:
                person_counter[ord(ans)-97] = True
            group_counter = [x and y for x, y in zip(group_counter, person_counter)]
        unique_answers += sum(group_counter)
    print(unique_answers)