ch = input("Enter any character : ")
if(ch >= 'A' and ch <='Z'):
    ch = ch.lower()
    print("The entered character was a upper case. In lowercase it is : " + ch)
else:
    ch = ch.upper()
    print("The entered character was a lower case. In uppercase it is : " + ch)
    
