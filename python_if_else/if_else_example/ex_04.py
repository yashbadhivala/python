val1=10
val2=20
val3=30

if(val1>val2):
    if(val1>val3):
        print(f"{val1} is biggest.")
elif(val2>val3):
    if(val2>val1):
        print(f"{val2} is biggest.")
else:
    print(f"{val3} is biggest.")