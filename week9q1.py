def print_pascals_triangle(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    triangle = [[1]]
    
    for i in range(1, n):
        last_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, len(last_row)):
            new_value = last_row[j - 1] + last_row[j]
            new_row.append(new_value)
        
        new_row.append(1)
        
        triangle.append(new_row)
    
    for row in triangle:
        print(row)

print_pascals_triangle(5)
