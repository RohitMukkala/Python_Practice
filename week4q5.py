char = input("Enter a character: ")
if 67<=ord(char)<=90:
    print(f"'{char}' is Uppecase")
elif 97<=ord(char)<=122:
    print(f"'{char}' is LowerCase")
else:
    print("Invalid")