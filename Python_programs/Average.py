n = int(input("Enter a number : "))
avg = 0.0
s = 0
for i in range(1,n+1):
    s = s + i
avg = s/i
print("The sum of first",n,"natural numbers is",s)
print("The average of first",n,"natural numbers is",avg)
