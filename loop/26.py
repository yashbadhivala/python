#factors of 6 = 1 2 3 6 [if sum of factor=number  1 2 3=6  ] 6 ne include na karva.

val=int(input("enter value :"))
sum=0
temp=val

for i in range(1,val)[::-1]:
    if(val%i==0):
        sum+=i

print(sum)

if(sum==temp):
    print("perfect number .")
else:
    print("not perfect .")