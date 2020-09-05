ch = input("Enter any character : ")
num_count = 0
up_count = 0
low_count = 0
if(ch >= '0' and ch <= '0'):
    num = num + 1
elif(ch >= 'a' and ch <= 'z'):
    low_count = low_count + 1
elif(ch >= 'A' and ch <= 'Z'):
    up_count = up_count + 1
while(ch != '*'):
    ch = input("Enter any character : ")
    if(ch >= '0' and ch <= '0'):
        num_count = num_count + 1
    elif(ch >= 'a' and ch <= 'z'):
        low_count = low_count + 1
    elif(ch >= 'A' and ch <= 'Z'):
        up_count = up_count + 1
print("Number of lowercase characters are : ",low_count)
print("Number of uppercase characters are : ",up_count)
print("Number of numerals are : ",num_count)
    
