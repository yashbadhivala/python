char=input("enter character (a-z) or (A-Z) :")

#print(f"{ord(char)}")

asc=ord(char)

if(asc>=65 and asc<=90):
    #upper to lower
    asc=asc+32
    print(f"{chr(asc)}")
elif(asc>=97 and asc<=122):
    #lower to upper
    asc=asc-32
    print(f"{chr(asc)}")
else:
    print("invalid")
