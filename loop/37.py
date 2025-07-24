#reverse

val=int(input("enter number :"))

digit=0
rev=0

while(val>0):
    digit=val%10
    rev=(rev*10)+digit
    val=val//10

print(rev)