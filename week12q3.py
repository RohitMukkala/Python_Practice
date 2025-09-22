def insert_in_middle(original, to_insert):
    middle_index = len(original) // 2
    new_string = original[:middle_index] + to_insert + original[middle_index:]
    return new_string

# Get input from the user
original_string = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

# Call the function and get the result
result_string = insert_in_middle(original_string, string_to_insert)

# Print the result
print(f"Resulting string: {result_string}")
