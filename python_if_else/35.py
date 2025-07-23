a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=0
print("before :")

print(f"{a} {b}")

print("after :")

if(not(a==b)):
    c=a
    a=b
    b=c
    print(f"{a} {b} ")

else:
    print("both are same.....")
    