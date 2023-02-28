# Noel Stallworth
# TIME: 2021/9/30 22:49
a = sorted([-12, -1, 0, 1, 3])
print(a)

b = sorted([-12, -1, 0, 1, 3], key=abs)
print(b)

c = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(c)
