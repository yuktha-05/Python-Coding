p = int(input("Enter a value : ")) #principal value
r = int(input("Enter a percentage value : "))#simple interest rate in %
t = int(input("Enter a value : "))#years
SI = (p*r*t)/100
CI = p*((1+(r/100))**t)
print("Simple Interest = ",SI)
print("Compound Interest = ",CI)
