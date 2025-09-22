def print_squares_list():
    squares_list = []
    
    for num in range(1, 31):
        square = num ** 2
        squares_list.append(square)
    
    print("List of squares from 1 to 30:")
    print(squares_list)


print_squares_list()
