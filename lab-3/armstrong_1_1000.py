for i in range(1,1001):
    n=len(str(i))
    sum=0
    temp=i
    while(temp>0):
        sum=sum+((temp%10)**n)
        temp=temp//10
    if(sum==i):
        print(i)
    else:
        continue
