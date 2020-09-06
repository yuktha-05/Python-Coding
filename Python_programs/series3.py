n = int(input("Enter a number : "))
s = 0.0
for i in range(1,n+1):
    a = float(i)/(i+1)
    s = s+a
print("The sum of series is",s)
