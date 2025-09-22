user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

n = len(numbers)

# Bubble Sort to sort the list in ascending order
for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Find the second largest number
largest = numbers[-1]
second_largest = None

for i in range(n - 2, -1, -1):
    if numbers[i] < largest:
        second_largest = numbers[i]
        break

if second_largest is not None:
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not have enough unique numbers.")
