total_prime = 0
total_composite = 0
while(1):
    num = int(input("Enter a number : "))
    if(num == -1):
        break
    iscomposite = 0
    for i in range(2,num):
        if(num%i == 0):
            iscomposite = 1
            break
    if(iscomposite == 1):
        total_composite += 1
    else:
        total_prime += 1
print("Total Composite Numbers : ",total_composite)
print("Total Prime Numbers : ",total_prime)
