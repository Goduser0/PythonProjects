# Noel Stallworth
# Time: 2021-7-20  15:06
for i in range (-100,1600) :
    for j in range(101):
        if i+100==j**2:
            for k in range(101):
                if i+100+168==k**2:
                    print (i,'+100=',j,'*',j)
                    print (i,'+168=',k,'*',k)