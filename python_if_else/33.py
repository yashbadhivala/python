unit=int(input("enter units :"))
bill=0

if(unit<=50):
    bill=unit*0.5
elif(unit<=100):
    bill=25+(unit-50)*0.75
elif(unit<=250):
    bill=100+(unit-150)*1.20
elif(unit>250):
    bill=220+(unit-250)*1.5
else:
    print("invalid.....")
    
sur=bill*0.2
total=bill+sur

print(total)