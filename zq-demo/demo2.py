# Noel Stallworth
# Time: 2021-7-20  14:17
i=int(input('Please enter the profit'))
arr=[0,1e5,2e5,4e5,6e5,10e5]
rat=[0.1,0.075,0.05,0.03,0.015,0.0]
sum=0
for idx in range(1,6) :
    if i>=arr[idx] :
        sum+=(arr[idx]-arr[idx-1])*rat[idx-1]
    else :
        sum+=(i-arr[idx-1])*rat[idx-1]
        break

print('ans=',sum)

