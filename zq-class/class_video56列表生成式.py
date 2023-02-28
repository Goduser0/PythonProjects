# Noel Stallworth
# Time: 2021-7-15  15:06
list1=[i+1 for i in range(1,10)]
print(list1)

list2=[x if x%3 ==0 else x**2 for x in range(0,10,2)]
print(list2)

list3=[x for x in range(0,20) if x%3 ==0]
print(list3)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str) == True]
print(L2)
