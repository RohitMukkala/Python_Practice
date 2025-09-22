user_input = input("Enter elements for the tuple separated by commas (e.g., 1,2,3,4,5,6): ")
elements = tuple(map(int, user_input.split(',')))

if len(elements) >= 4:
    fourth_element = elements[3]
    fourth_from_last_element = elements[-4]
    print("The 4th element is:", fourth_element)
    print("The 4th element from the last is:", fourth_from_last_element)
else:
    print("The tuple does not have enough elements.")
