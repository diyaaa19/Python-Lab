x=int(input("Enter a number: "))
f=0
for i in range(1,x+1):
    if(x%i==0):
        f+=1
    
if(f==2):
    print("Prime number")
else:
    print("Not prime")
