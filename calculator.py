print("1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n")
num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
choice=int(input("Enter your choice : "))
if(choice==1):
    print(num1+num2)
elif(choice==2):
    print(num1-num2)
elif(choice==3):
    print(num1/num2)
elif(choice==4):
    print(num1*num2)
else:
    print("Invalid Choice")