print("nCr")
n=int(input("Enter value of n:"))
r=int(input("Enter the value of r:"))
nfact=1
rfact=1
nrfact=1
for i in  range(1,n+1):
    nfact=nfact*i
for i in range(1,r+1):
    rfact=rfact*i
for i in range(1,(n-r)+1):
    nrfact=nrfact*i
print("Value of nCr is :",int(nfact/(rfact*nrfact)))