# Noel Stallworth
# Time: 2021-7-20  15:37
def dib(x):
    if x==0 :
        ans=0
    elif x==1 :
        ans=1
    else :
        ans=dib(x-1)+dib(x-2)

    return ans
for i in range(11):
    print(dib(i))

