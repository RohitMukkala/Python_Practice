
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50,
    'f': 60
}

top_3 = []

for key, value in my_dict.items():
    
    top_3.append((value, key))

for i in range(len(top_3)):
    for j in range(i + 1, len(top_3)):
        if top_3[j][0] > top_3[i][0]:
            top_3[i], top_3[j] = top_3[j], top_3[i]


top_3_values = top_3[:3]


print("Top 3 values and their corresponding keys:")
for value, key in top_3_values:
    print(f"Key: {key}, Value: {value}")
