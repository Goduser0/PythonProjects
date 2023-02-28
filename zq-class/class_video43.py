# Noel Stallworth
# Time: 2021-7-15  10:59
for i in range(5):
    for j in range(1,i+2):
        if j==1 :print('*',end='')
        if 1<j<i+1 :print(' ',end='')
        if (j==i+1 and j!=1 ): print('*')
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()