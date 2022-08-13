
fruit = {"Orange": "Sweet", "Lemon": "Sour", "grape": "Sweet and small", "Apple": "Sweet and Red"}

# Pritining Dictionary
print(fruit)

# Accessing element from dictionary with the help of key
print(fruit['Orange'])

# Adding a new Key Value pair
fruit["Peer"] = "Odd Shaped Apple"
print(fruit)

# Duplicating a key
fruit["Peer"] = "Great with tequila"
print(fruit)

# Deleting a key value
del fruit["Peer"]
print(fruit)

# Deleting a whole dictionary
# del fruit
# print(fruit)

# Get method with default value
print(fruit.get("Key", "Default Value"))

# Checking key is there or not
print("Orange" in fruit)
print("Key2" in fruit)

# Iterating through Dict
for snack in fruit:
    print(fruit[snack])

# Getting the list of keys
sorted_keys = (fruit.keys())
print(type(sorted_keys))
print(sorted_keys)
sorted_values = fruit.values()
print(sorted_values)

#
print(fruit.items())

# Combining two dictionaries
veg = {'Cabbage': "Everyone's favorite",
       'Tomato': 'Red'}
fruit.update(veg)
print(fruit)
print(veg)
veg.update(fruit)
print(veg)
print(fruit)


# Removing all elements from dictiinary
fruit.clear()
print(fruit)





