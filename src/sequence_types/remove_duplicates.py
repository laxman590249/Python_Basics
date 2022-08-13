

dictionanry = {"key1": "value1", "key2": "value2", "key3": "value1", "key4": "value2", "key5": "value2", "key6": "value3"}

values = list(dictionanry.values())
keys = list(dictionanry.keys())

for key in keys:
    if values.count(dictionanry[key]) > 1:
        values.remove(dictionanry[key])
        del dictionanry[key]

print(dictionanry)