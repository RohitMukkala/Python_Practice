user_input1 = input("Enter numbers for the first list separated by spaces: ")
list1 = list(map(int, user_input1.split()))

user_input2 = input("Enter numbers for the second list separated by spaces: ")
list2 = list(map(int, user_input2.split()))

intersection_list = []

# Find common elements
for item in list1:
    if item in list2 and item not in intersection_list:
        intersection_list.append(item)

print("The intersection of the two lists is:", intersection_list)
