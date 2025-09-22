input_string = input("Enter a string: ")

word_list = []
word = ""

for char in input_string:
    if char != ' ':
        word += char
    else:
        if word:
            word_list.append(word)
            word = ""
if word:
    word_list.append(word)

print(word_list)
