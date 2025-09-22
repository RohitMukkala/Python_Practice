def find_largest_number(numbers):
    if not numbers:
        return None
    
    largest_number = numbers[0]
    for number in numbers[1:]:
        if number > largest_number:
            largest_number = number
            
    return largest_number

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

largest_number = find_largest_number(numbers)
if largest_number is not None:
    print("The largest number in the list is:", largest_number)
else:
    print("The list is empty.")
