# Noel Stallworth
# Time: 2021-7-15  10:17

#for item in 'python':
#   print(item)

#sum=0
#for num in range(2,101,2):
#    sum+=num
#print(sum)

#水仙花数
for num in range(100,1000):
    bai=int(str(num)[0])
    shi=int(str(num)[1])
    ge=int(str(num)[2])
    if(num==bai**3+shi**3+ge**3):
        print (num)