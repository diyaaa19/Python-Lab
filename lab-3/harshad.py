a=int(input("Enter a number :"))
n=len(str(a))
temp=a
sum=0
while temp>0:
    r=temp%10
    sum+=r
    temp=temp//10
if(a%sum==0):
    print("Harshad Number")
else:
    print("Not a harshad number")