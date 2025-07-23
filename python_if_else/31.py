eng=int(input("enter marks of english :"))
math=int(input("enter marks of math :"))
sci=int(input("enter marks of science :"))
his=int(input("enter marks of history :"))
com=int(input("enter marks of com :"))

res=(eng+math+sci+his+com)/5

if(res>=90):
    print("grade A+")
elif(res>=80):
    print("grade A")
elif(res>=70):
    print("grade B+")
elif(res>=60):
    print("grade C+")
elif(res>=40):
    print("grade D+")
else:
    print("fail.")