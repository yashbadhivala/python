#sum of second and second last.

val=int(input("enter number :"))

s_l_d=(val//10)%10

while(val>10):
    s_d=val%10
    val=val//10

sum=s_d + s_l_d
print(f"second number is {s_d}.")
print(f"second last number is {s_l_d}.")
print(f"sum  is {sum}.")