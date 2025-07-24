#sum of all digit.

val=int(input("enter number :"))
digit=0
sum=0

while(val>0):
    digit=val%10
    sum=sum+digit
    val=val//10

print(sum)