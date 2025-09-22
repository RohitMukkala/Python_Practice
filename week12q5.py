def add_prefix_to_lines(text, prefix):
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(prefix + line)
    return '\n'.join(new_lines)

input_text = ""
while True:
    line = input()
    if line == "":
        break
    input_text += line + "\n"

prefix = input()

result_text = add_prefix_to_lines(input_text, prefix)

print(result_text)
