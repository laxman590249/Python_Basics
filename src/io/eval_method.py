
my_tuple = 'This is 1', 'This is 2', 'This is 3', 'This is 4', ('This is 5_1', 'This is 5_2')
print(my_tuple)
with open('expression.txt', 'w') as file:
    print(my_tuple, file=file)

with open('expression.txt', 'r') as file:
    contents = file.readline()

expression = eval(contents)
print(expression)
print(type(expression))




