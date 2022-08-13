
# 1 way to create a set
animal_set = {'Dog', 'Cat', 'Horse', 'Mouse', 'Cow'}
print(animal_set)

# 2 way to create set
wild_animal_set = set(['lion', 'tiger', 'elephant', 'deer'])
print(wild_animal_set)

# Iterating through Set
for animal in animal_set:
    print(animal)

# Adding new item into Set
wild_animal_set.add('Panther')
print(wild_animal_set)

# Union/Intersection/substract on two sets
even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuple = (4, 8, 9, 16, 25)
square_set = set(square_tuple)

# Union
union_set = even.union(square_tuple)
print(union_set)

# intersection
intersection_set = even.intersection(square_set)
print(intersection_set)

# Substracting -
substract_set = even - square_set
print(substract_set)
substract_set2 = even.difference(square_set)
print(substract_set2)

# Symmetric Difference
print(even.symmetric_difference(square_set))

# difference_update
even.difference_update(square_set)
print(even)

# deleting an element from Set

set1 = {1, 2, 3, 4, 5}
set1.remove(1)
set1.discard(2)
print(set1)

# If element not found, this does not give error
set1.discard(8)

# If not found the it throws exception
try:
    set1.remove(8)
except KeyError:
    print('Item not found...')

# sub set and super set
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4}

print(set2.issubset(set1))
print(set1.issuperset(set2))

