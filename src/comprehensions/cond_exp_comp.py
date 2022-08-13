
menu = [['Egg', 'Meat', 'Spam'],
        ['Egg', 'Meat', 'Dahi'],
        ['Egg', 'Meat', 'Icecrea'],
        ['Icecrea', 'Dahi', 'Spam'],
        ['Egg', 'Meat', 'Dhokla']]

food = [meal if 'Spam' not in meal else 'Skipped records' for meal in menu]

print(food)
