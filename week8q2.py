user_input = input("Enter elements for the tuple separated by commas (e.g., 1,2,3,4,5,1,2): ")
elements = tuple(map(int, user_input.split(',')))

count_dict = {}
for item in elements:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1


repeated_items = [item for item, count in count_dict.items() if count > 1]

print("Repeated items in the tuple are:", repeated_items)
