#armstrong or not

val=int(input("enter number :"))
temp=val
digit=0
sum=0

while(val>0):
    digit=val%10
    sum=sum + ( digit ** 3 )
    val=val//10
    
print(f"sum is {sum}")    
if(temp==sum):
    print("this is armstrong number.")
else:
    print("this is not armstrong number.")