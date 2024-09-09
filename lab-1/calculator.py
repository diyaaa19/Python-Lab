print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
print("\n")
x=int(input("Enter your choice from 1-4 :"))
if(x==1):
    print("Sum:",a+b)
elif(x==2):
    print("Difference:",a-b)
elif(x==3):
    print("Product:",a*b)
elif(x==4):
    print("Quotient:",a/b)
else:
    print("Invalid Choice!")