

burgers = ['Beef', 'Chicken', 'Egg']
toppings = ['Chees', 'Bean', 'Spam']

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

for meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meals)
