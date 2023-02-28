# Noel Stallworth
# TIME: 2021/9/17 22:27

a = abs(-2)
print(a)
f = abs  # 变量指向函数
b = f(-0.5)
print(b)
print()


def add(x, y, sum):  # 函数add 接收 函数sum 作为参数，故add为高阶函数
    return sum(x) + sum(y)


result = add(-5.4, 5.2, int)
print(result)

