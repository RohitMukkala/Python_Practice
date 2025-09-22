def are_anagrams(str1, str2):
    # Helper function to convert string to lowercase
    def to_lower(s):
        result = ""
        for char in s:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
        return result

    # Helper function to remove spaces from string
    def remove_spaces(s):
        result = ""
        for char in s:
            if char != " ":
                result += char
        return result

    # Helper function to count characters in string
    def count_characters(s):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count

    # Normalize strings
    str1 = remove_spaces(to_lower(str1))
    str2 = remove_spaces(to_lower(str2))

    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Count characters in both strings
    count1 = count_characters(str1)
    count2 = count_characters(str2)

    # Compare character counts
    return count1 == count2

# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function and get the result
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
