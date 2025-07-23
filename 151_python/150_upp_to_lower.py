char=input("enter character (A-Z):")
print(f"ascii of {char} is {ord(char)}")

low=(ord(char)+32)
print(f"{char}'s lowercase is {chr(low)}")