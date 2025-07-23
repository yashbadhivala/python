a=int(input("enter choice 2 or 3 :"))

b=0
c=0
d=0

if(a==2):
    b=int(input("enter number 1 :"))
    c=int(input("enter number 2 :"))
    print(f"sum of {b} and {c} is {b+c}")
elif(a==3):
    b=int(input("enter number 1 :"))
    b=int(input("enter number 2 :"))
    d=int(input("enter number 3 :"))
    print(f"sum of {b} and {c} and {d} is {b+c+d}")      
else:
    print("invalid...")

    