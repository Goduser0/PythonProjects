# Noel Stallworth
# Time: 2021-7-20  15:26
for i in range(3):
    x=int(input('enter the number'))
    if i==0 :
        a=x
    if i==1 :
        if x>a :
            b=x
        else :
            b=a
            a=x
    if i==2 :
        if x<a :
            print(x,a,b)
        elif  a<=x<b :
            print(a,x,b)
        else :
            print(a,b,x)

