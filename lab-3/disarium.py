a=int(input("Enter a number: "))
n=len(str(a))
temp=a
sum=0
while temp>0:
    r=(temp%10)
    sum+=r**n
    temp=temp//10
    n=n-1
if(sum==a):
    print("disarium number")
else:
    print("Not a disarium number")
