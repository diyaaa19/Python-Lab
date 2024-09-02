a=int(input("Enter a number : "))
f=0

for i in  range(1,a+1):
    if(a%i==0):
        f+=1
        
if(f==2):
    print("Prime number")
else:
    print("Not a prime")