with open('input.txt', 'r') as f:
    input_file = f.read().split('\n')
input_file = [int(i) for i in input_file]
print(next(t for t in [[n * x for x in input_file[i:-1] if (n+x) == 2020] for i, n in enumerate(input_file)] if len(t)> 0))