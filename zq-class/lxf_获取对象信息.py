import types

a = type(123)
print(a)
b = type(abs)
print(b)


def fn(i):
    return i * i


print(type(fn) == types.FunctionType)

# isinstance

print(isinstance(123, int))

print(dir('ABC'))

obj = 1
hasattr(obj, 'x')  # 有属性‘x’吗？
setattr(obj, 'y', 19)  # 设置属性‘y’为19
getattr(obj, 'y')  # 获取属性‘y’
getattr(obj, 'y', 404)  # 获取属性‘z’，如果不存在，返回默认值404

