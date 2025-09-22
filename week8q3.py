user_input = input("Enter elements for the tuple separated by commas (e.g., 1,2,3,4,5): ")
elements = tuple(map(int, user_input.split(',')))

search_element = int(input("Enter the element to search for: "))

if search_element in elements:
    print(f"The element {search_element} exists in the tuple.")
else:
    print(f"The element {search_element} does not exist in the tuple.")
