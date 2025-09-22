user_input = input("Enter strings separated by commas (e.g., apple,banana,kiwi): ")
strings = [s.strip() for s in user_input.split(',')]

n = len(strings)

# Bubble Sort to sort the list based on the length of the strings
for i in range(n):
    for j in range(n - i - 1):
        if len(strings[j]) > len(strings[j + 1]):
            strings[j], strings[j + 1] = strings[j + 1], strings[j]

print("The list sorted by the length of the elements is:", strings)
