user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

for i in range(1, len(numbers), 2):
    print(numbers[i])
