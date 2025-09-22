"""Write a Python program to find frequency of each digit in a given integer."""

number = int(input("Enter an Integer: "))
frequency = {str(digit): 0 for digit in range(10)}
number_str = str(number)

for digit in number_str:
    if digit in frequency:
        frequency[digit]+=1
print(frequency)