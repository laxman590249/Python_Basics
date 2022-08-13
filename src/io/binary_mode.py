#
# # Passing integer values inside a list
# with open('binary', 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))
#
#
# with open('binary', 'br') as file:
#     for bin in file:
#         print(bin)


# # Passing integer values inside a list
# with open('binary', 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open('binary', 'br') as file:
#     for bin in file:
#         print(bin)

# Inserting integers with variables

a = 65534
b = 65535
c = 65536
d = 2998302

with open('binary2', 'bw') as file:
    file.write(a.to_bytes(2, 'big'))
    file.write(b.to_bytes(2, 'big'))
    file.write(c.to_bytes(4, 'big'))
    file.write(d.to_bytes(4, 'big'))
    file.write(d.to_bytes(4, 'little'))

with open('binary2', 'br') as file:
    a = int.from_bytes(file.read(2), 'big')
    b = int.from_bytes(file.read(2), 'big')
    c = int.from_bytes(file.read(4), 'big')
    d = int.from_bytes(file.read(4), 'big')
    e = int.from_bytes(file.read(4), 'little')

print('A : ', a)
print('B : ', b)
print('C : ', c)
print('D : ', d)
print('E : ', e)





