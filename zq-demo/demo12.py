# Noel Stallworth
# Time: 2021-7-22  14:35
from math import sqrt
for i in range(101,201) :
    for j in range(2,int(sqrt(i+1))) :
        if i%j==0 : break
        if j==int(sqrt(i))-1 and i%int(sqrt(i)-1) !=0 :
            print(i)

