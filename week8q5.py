
list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_value = 100

new_list_of_tuples = [(x[0], x[1], new_value) for x in list_of_tuples]

print("List after replacing the last value of each tuple:", new_list_of_tuples)
