
def replace_a_with_b(input_string):
    if 'a' not in input_string:
        print("The character 'a' is not present in the string.")
        return input_string
    else:
        return input_string.replace('a', 'b')

input_string = input("Enter a string: ")

result_string = replace_a_with_b(input_string)

print(f"Resulting string: {result_string}")
