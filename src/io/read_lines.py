
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    print(line, end='')

# printing file backward
for line in lines[::-1]:
    print(line, end='')

# using read()

with open('sample.txt', 'r') as file:
    lines = file.read()
    print(lines)

for char in lines[::-1]:
    print(char, end='')



