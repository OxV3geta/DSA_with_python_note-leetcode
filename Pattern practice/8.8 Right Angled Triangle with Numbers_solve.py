def right_number_triangle(n):
    num_triangle = []
    
    for i in range(1,n+1):
        num_triangle.append((f"{i}")*i)
    
    return num_triangle

print(right_number_triangle(5))