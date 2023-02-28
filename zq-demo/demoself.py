# Noel Stallworth
# Time: 2021-7-20  15:59
def findMinAndMax(L):
    if L== None: return (None, None)
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i > max: max = i
            if i < min: min = i
    return (min,max)

if findMinAndMax(None) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')