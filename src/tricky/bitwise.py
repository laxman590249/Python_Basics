
n = 10

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
    # if num >= 1:
    #     DecimalToBinary(num // 2)
    # print(num % 2, end='')
    string = ''

    while (True):
        temp = num
        if num > 1:
            num = num // 2
        string += str(temp % 2)
        if num <= 1:
            string += str(num)
            break
    print(string[::-1])






# Driver Code
if __name__ == '__main__':
    # decimal value
    dec_val = 8

    # Calling function
    DecimalToBinary(dec_val)


