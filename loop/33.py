#sum of first and last digit.

val=int(input("enter value :"))
l_d=val%10


while(val>0):
    f_d=val%10
    val=val//10

sum=f_d + l_d
print(f"this is first digit {f_d}.")
print(f"this is last digit {l_d}.")
print(f"sum  is {sum}.")