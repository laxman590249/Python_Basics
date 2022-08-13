
# Code 1

# def A():
#     __name__ = 'B'
#     def __name__():
#         return 'C'
# print(A.__name__)


#code 2
class A:
    def __name__(self):
        return "B"

    def C(self):
        __name__ = "D"
        return "E"

    __name__ = "F"

print(A.__name__, end=",")
print(A.C.__name__, end=",")
print(A().__name__)
