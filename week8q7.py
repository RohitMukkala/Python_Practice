
list_of_tuples = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]


dictionary = {}

for item in list_of_tuples:
    key = item[0]
    value = item[1]
    dictionary[key] = value


print("Dictionary:", dictionary)
