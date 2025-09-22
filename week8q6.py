
list_of_tuples = [(1, 2), (), (3, 4), (), (5,)]

filtered_list_of_tuples = [t for t in list_of_tuples if t]


print("List after removing empty tuples:", filtered_list_of_tuples)
