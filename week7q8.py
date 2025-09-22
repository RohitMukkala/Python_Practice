user_input1 = input("Enter numbers for the first list separated by spaces: ")
list1 = list(map(int, user_input1.split()))

user_input2 = input("Enter numbers for the second list separated by spaces: ")
list2 = list(map(int, user_input2.split()))

union_list = []

# Add elements from the first list to the union list
for item in list1:
    if item not in union_list:
        union_list.append(item)

# Add elements from the second list to the union list if not already present
for item in list2:
    if item not in union_list:
        union_list.append(item)

print("The union of the two lists is:", union_list)
