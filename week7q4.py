user_input1 = input("Enter numbers for the first list separated by spaces: ")
list1 = list(map(int, user_input1.split()))

user_input2 = input("Enter numbers for the second list separated by spaces: ")
list2 = list(map(int, user_input2.split()))

merged_list = list1 + list2

for i in range(len(merged_list)):
    for j in range(i + 1, len(merged_list)):
        if merged_list[i] > merged_list[j]:
            merged_list[i], merged_list[j] = merged_list[j], merged_list[i]

print("The merged and sorted list is:", merged_list)
