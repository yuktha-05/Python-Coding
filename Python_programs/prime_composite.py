num = int(input("Enter a number : "))
iscomposite = 0
for i in range(2,num):
    if(num%i == 0):
        iscomposite = 1
        break
if(iscomposite == 1):
    print(num,"is a Composite Number")
else:
    print(num,"is a Prime Number")
