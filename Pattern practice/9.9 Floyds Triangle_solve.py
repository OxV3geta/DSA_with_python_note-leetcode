def generate_floyds_triangle(n):
    # Initialize an empty list to store the rows of the triangle
    triangle = []
    
    # Initialize the first number to be used in the triangle
    current_num = 1
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Create a row by collecting the next i numbers
        row = ' '.join(str(current_num + j) for j in range(i))
        # Append the row to the list
        triangle.append(row)
        # Update the current number for the next row
        current_num += i
    
    # Return the list of rows
    return triangle

print(generate_floyds_triangle(5))