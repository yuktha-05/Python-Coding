a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
print(a,b,c)
S = (a+b+c)/2
area = (S*(S-a)*(S-b)*(S-c))**0.5
print("Area = " + str(area))
