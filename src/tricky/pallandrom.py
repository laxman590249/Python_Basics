

string = "ArrayList"

array = list(string)
#
# start = 0
# end = len(string)-1
#
# while end > start:
#     if array[start] != array[end]:
#         break
#     start += 1
#     end -= 1
#
# if end > start:
#     print("Not")
# else:
#     print("Yes")

start = 0
end = len(string)-1
while end > start:
    temp = array[start]
    array[start] = array[end]
    array[end] = temp
    start += 1
    end -= 1

print(array)
