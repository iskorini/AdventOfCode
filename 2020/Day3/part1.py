with open('./input.txt', 'r') as f:
    input = f.read()
trees = 0
x = 0 
for row in input.splitlines():
    trees += int(row[x] == '#')
    x = (x+3)%len(row)
print(trees)

