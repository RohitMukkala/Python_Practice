n = input("Enter a character: ")
if 65<=ord(n)<=90 or 97<=ord(n)<=122:
    print(f"{n} is an alphabet.")
else:
    print(f"{n} is not an alphabet.")