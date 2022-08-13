
list_fruites = ['Apple', 'Banana', 'Orange', 'Cheeku']
list_fruites.append('Strawberry')

for fruit in list_fruites:
    print(fruit)

odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]

numbers = odd + even
numbers_in_order = sorted(numbers)
print("Using Sorted Method", numbers_in_order)
print(sorted(numbers) == numbers_in_order)
numbers.sort() # This will reflect in same list
print("Return of Sort Method", numbers.sort())
print("Sorted List :",numbers)

# List Constructors

empty_list = list() #1
character_list = list("Hello") #2

print(empty_list)
print(character_list)

even = [2, 4, 6, 8]
another_1 = even
another_2 = list(even) #3
even.sort(reverse=True)

print(even == another_1) # Poinitng to same list
print(even == another_2) # Its a different list

print(even is another_1) # Poinitng to same list
print(even is another_2) # Its a different list






