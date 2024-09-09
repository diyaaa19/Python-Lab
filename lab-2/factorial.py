n=int(input("Enter a number: "))
fact=1
if(n<0):
    print("Enter a positive number")
if(n==0):
    print("Factorial is 1")
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)