# Noel Stallworth
# Time: 2021-7-22  15:04
zsj=[2]
from math import sqrt
for i in range(101) :
    for j in range(2,i) :
        if i%j==0 : break
        if j==i-1 and i%j !=0 :
          zsj.append(i)
print(zsj)
cjs=[]
def fjzys(k):
    while(1):
        for zs in zsj :
            if k==1 :
                return cjs
            elif k%zs ==0 :
                cjs.append(zs)
                k=k//zs
                zs=zsj[0]

while(1) :
    cjs=[]
    num=int(input('Enter the number'))
    print(fjzys(num))