a=int(input("enter number 1 :"))
b=int(input("enter number 2 :"))
char=input("enter operation (+,-,*,/,%) :")

if(char=='+'):
    print(f"addition is {a+b}")
elif(char=='-'):
    print(f"substracion is {a-b}")
elif(char=='*'):
    print(f"multiplication is {a*b}")
elif(char=='/'):
    print(f"division is {a//b}")
elif(char=='%'):
    print(f"modulous is {a%b}")
else:
    print("invalid")
    