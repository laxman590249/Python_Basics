import timeit

text = input("Please enter your text: ")

output = []

for_loop = """\
for x in text.split():
    output.append(len(x))
print(output)
"""

# type your solution here:

comp = """\
output_2 = [len(y) for y in text.split()]
print(output_2)
"""
