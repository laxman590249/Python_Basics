
menu = [['Egg', 'Meat', 'Spam'],
        ['Egg', 'Meat', 'Dahi'],
        ['Egg', 'Meat', 'Icecrea'],
        ['Icecrea', 'Dahi', 'Spam'],
        ['Egg', 'Meat', 'Dhokla']]

result = [meal for meal in menu if 'Spam' not in meal]

print(result)
