def get_first_three_characters(s):
    if len(s) < 3:
        return s
    return s[:3]

input_string = input("Enter a string: ")


result_string = get_first_three_characters(input_string)

print(f"Resulting string: {result_string}")
