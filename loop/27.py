#highest factor...

val=int(input("enter number :"))

for i in range(val-1,1,-1):
    if(val%i==0):
        print(i)
        break
        
        
    