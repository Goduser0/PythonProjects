# Noel Stallworth
# Time: 2021-7-22  14:59
for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    if i==a**3+b**3+c**3 : print (i)