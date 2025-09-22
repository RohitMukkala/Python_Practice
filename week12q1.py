input_string = input("Enter a string: ")
char = input("Enter the specified character: ")
index = input_string.find(char)
if index != -1:
    result_string = input_string[:index]
else:
    result_string = input_string
print(f"Resulting string: {result_string}")
