# Noel Stallworth
# TIME: 2021/9/30 22:16

def choose(n):
    return n % 3


a = filter(choose, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(a))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def is_palindrome(n):
    _str = str(n)
    length = int(len(_str)/2)
    if length != 0:
        for i in range(0, length):
            if _str[i] != _str[-(i+1)]:
                return 0
    return 1


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
