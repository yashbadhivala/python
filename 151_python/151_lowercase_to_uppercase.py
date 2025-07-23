char=input("enter character (a-z) :")

print(f"ascii value of {char} is {ord(char)}")

upper=(ord(char)-32)
print(f"{char}'s uppercase is {chr(upper)}")