
def remove_nth_index_char(input_string, n):
    if n < 0 or n >= len(input_string):
        return "Invalid index"
    return input_string[:n] + input_string[n+1:]

input_string = input("Enter a non-empty string: ")
n = int(input("Enter the index of the character to remove: "))


result_string = remove_nth_index_char(input_string, n)


print(f"Resulting string: {result_string}")
