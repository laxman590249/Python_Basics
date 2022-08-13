import pickle

tuples = ('First Line', 'Second Line', ((1, 'First Sub object'), (2, 'Second Sub Object'), (3, 'Third Subobje')))

with open('file_1.pickle', 'wb') as pickle_file:
    pickle.dump(tuples, pickle_file)

with open('file_1.pickle', 'rb') as pickle_file:
    tuples_2 = pickle.load(pickle_file)

print(tuples_2)

