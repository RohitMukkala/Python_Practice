user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

if len(numbers) < 2:
    print("The list does not have enough unique numbers.")
else:
    largest = max(numbers[0], numbers[1])
    second_largest = min(numbers[0], numbers[1])
    
    for number in numbers[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
            
    print("The second largest number in the list is:", second_largest)
