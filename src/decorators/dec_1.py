

def new_decorator(orignal_funxtion):

    def wrap_function(v):
        print('Some Extra code', v)

        orignal_funxtion()

        print('Some other extra code')

    def wrap_function_2(v):
        print('Some Extra code New', v)

        orignal_funxtion(v)

        print('Some other extra code')

        return wrap_function

    return wrap_function_2


# def fun_needs_decorator():
#     print('I need a decorator...!')
#
#
# my_dec = new_decorator(fun_needs_decorator)
# my_dec()

# The above lines can be converted by below statements.

@new_decorator
def fun_needs_decorator(v):
    print('I need a decorator...!')

r = fun_needs_decorator(2)
print(r)
