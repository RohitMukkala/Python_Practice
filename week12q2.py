sentence = input("Enter a sentence: ")

# Convert the sentence to a list of words by splitting on spaces
words = []
word = ""
for char in sentence:
    if char == " ":
        if word:
            words.append(word)
            word = ""
    else:
        word += char
if word:
    words.append(word)

# Create a dictionary to count occurrences of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the occurrences of each word
for word, count in word_count.items():
    print(f"'{word}': {count}")
