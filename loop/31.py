#count total digit in number 
count=0

val=int(input("enter number :"))

while(val>0):
    count+=1
    val=val//10
    
print(count)
    
    
    