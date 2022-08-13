
multi_letter_string = 'ww3school'
dict_result = {}

for i in multi_letter_string:
    dict_result[i] = dict_result.get(i, 0) + 1

print(dict_result)
