import shelve

with shelve.open('fruite_shelve') as fruit:
    fruit['Banana'] = 'Long'
    fruit['Orange'] = 'Circular'

    print(fruit['Banana'])
