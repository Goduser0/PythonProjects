# Noel Stallworth
# Time: 2021-7-22  14:16

def rab(a) :
    if a ==1 or a==2 : return 1
    else :
        return rab(a-1)+rab(a-2)

month=int(input('Pleasr Enter The Month'))
for i in range(1,month+1) :
    print ('第',i,'个月有',rab(i),'个兔子')
    print()