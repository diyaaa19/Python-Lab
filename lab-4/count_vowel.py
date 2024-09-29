a=input("Enter a string:")
vowels='aeiouAEIOU'
count=0
for i in a:
    if i in vowels:
        count+=1
print('Number of vowels in the string :',count)