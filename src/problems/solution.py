number = input()
array_string = input()
array_s = array_string.split(" ")
binary_array = []


def decimal_to_binary(num):
    binary = ""
    while num > 1:
        binary = binary + str(num % 2)
        num = num // 2
    if num > 0:
        return binary + str(num)
    else:
        return binary

b_max = 0

for n in array_s:
    b_number = decimal_to_binary(int(n))
    if len(b_number) > b_max:
        b_max = len(b_number)
    binary_array.append(b_number)

count = 0
max_count = 0

for i in range(0, b_max):
    count = 0
    for binary in binary_array:
        if i < (len(binary)) and binary[i] == '1':
            count += 1
    if max_count < count:
        max_count = count

print(max_count)









