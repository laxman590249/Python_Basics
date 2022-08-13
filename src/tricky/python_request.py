
numbers = [1, 2, 3, 100, 0, 3, 10, -2, 1, 2, 90]

max_multiple = 0
mul = 1
mul_negative = 1

for num in numbers:
    if num == 0:
        mul = 1
        continue
    if num < 0:
        if mul_negative < 0:
            mul_negative *= num
            mul = mul_negative
            mul_negative = 1
        else:
            mul_negative = mul * num
            mul = 1

    else:
        mul *= num
        if mul_negative != 1:
            mul_negative *= num

    if mul > max_multiple:
        max_multiple = mul

print(max_multiple)



