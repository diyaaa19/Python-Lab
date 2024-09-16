a=int(input("Enter a number : "))
n=len(str(a))
sum=0
temp=a
while(temp>0):
    sum=sum+((temp%10)**n)
    temp=temp//10
if(sum==a):
    print("armstrong number")
else:
    print("not an armstrong")
