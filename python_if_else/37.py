amt=int(input("enter amount :"))

if(amt>500):
    note=amt//500
    print(f"500's note is :{note}")
    amt=amt-(note*500)
    
if(amt>200):
    note=amt//200
    print(f"200's note is :{note}")
    amt=amt-(note*200)
    
if(amt>100):
    note=amt//100
    print(f"100's note is :{note}")
    amt=amt-(note*100)
    
if(amt>50):
    note=amt//50
    print(f"50's note is :{note}")
    amt=amt-(note*50)

if(amt>20):
    note=amt//20
    print(f"20's note is :{note}")
    amt=amt-(note*20)

if(amt>10):
    note=amt//10
    print(f"10's note is :{note}")
    amt=amt-(note*10)
    
if(amt>5):
    note=amt//5
    print(f"5's note is :{note}")
    amt=amt-(note*5)
    
if(amt>1):
    note=amt//1
    print(f"1's note is :{note}")
    amt=amt-(note*1)