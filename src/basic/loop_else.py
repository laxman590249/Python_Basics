
numbers = [4, 89, 31, 36, 50]

for number in numbers:
    if number % 8 == 0:
        print('Acceptable')
        break
else:
    print('Not Acceptable')

