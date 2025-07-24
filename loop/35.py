#sum of first and second last.

val=int(input("enter number :"))

s_d=(val//10)%10

while(val>0):
    f_d=val%10
    val=val//10

sum=f_d + s_d

print(f"first number is {f_d}")
print(f"second number is {s_d}")
print(f"sum is {sum}.")