num = int(input("Enter the number : "))
n = int(input("Till which power to be calcuated : "))
res = 1
for i in range(n):
    res = res*num
print(num,"raised to the power",n,"is",res)
