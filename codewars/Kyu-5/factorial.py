import math

def zeros(n):
    factorial = math.factorial(n)
    list_num = list(factorial)
    print(list_num)

    return factorial


print(zeros(5))