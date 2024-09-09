n=int(input("Enter the number : "))
temp=n
sum=0
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10

if(temp==sum):
    print("strong number")
else:
    print("not a strong number")
