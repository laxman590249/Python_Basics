

def fact_decorator(func):

    dict_result = {}
    l = []

    def inner_function(n):

        if not l:
            l.append(n/2)
            l.append(n)

        for ln in l:
            if dict_result.get(n):
                return dict_result.get(n)

            fact = func(ln)

            dict_result[ln] = fact

            print(dict_result)

        return fact

    return inner_function


@fact_decorator
def factorial(n):

    # if d.get(n-1):
    #     return dict_result.get(n-1)

    if n == 0:
        return 1

    return n * factorial(n-1)

# l = [500, 700, 1000, 1500, 2000]
# dict_result = {}
# for n in l:
#     # print(dict_result)
#     fact = factorial(n, dict_result)
#     dict_result[n] = fact
#     print(fact)

factorial(10)