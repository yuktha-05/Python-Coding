bn = int(input("Enter a binary number: "))
dn = 0
i = 0
while(bn != 0):
    r = bn%10 
    dn = dn + r*(2**i)
    bn = bn//10 
    i += 1
print("The decimal equivlent = ",dn)

