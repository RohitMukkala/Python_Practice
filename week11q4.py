input_string = input("Enter a string: ")
if len(input_string) > 1:
    temp = input_string[0]
    input_string = input_string[-1] + input_string[1:-1] + temp
print(f"Resulting string: {input_string}")
