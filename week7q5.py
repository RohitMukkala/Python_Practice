user_input = input("Enter sublists separated by commas (e.g., [1,2],[3,4],[5,6]): ")
sublists = eval(user_input)

for i in range(len(sublists)):
    for j in range(len(sublists) - i - 1):
        if sublists[j][1] > sublists[j + 1][1]:
            sublists[j], sublists[j + 1] = sublists[j + 1], sublists[j]

print("The sorted list according to the second element in sublist is:", sublists)
