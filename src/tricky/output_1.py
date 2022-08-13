

numbers = [1, 2, 3, 4, 5]

number = int(input('Please Enter Number, I will give you square of it : '))
squares = []

for number in numbers:
    squares.append(number ** 2)

pos = numbers.index(number)
print('Square is : ', squares[pos])

number = int(input('Please Enter Number, I will give you square of it : '))
squares = [number ** 2 for number in numbers]

pos = numbers.index(number)
print('Square is : ', squares[pos])






