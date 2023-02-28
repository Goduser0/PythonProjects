# Noel Stallworth
# TIME: 2021/9/17 22:46
from functools import reduce


def f(x):
    x *= x
    return x


def my_sum(x, y):
    x += y
    return x


a = map(f, [1, 2, 3])
print(list(a))
print()

c = map(str, [1, 2, 3, 4])
print(list(c))
print()

b = reduce(my_sum, [1, 2, 3])
print(b)
