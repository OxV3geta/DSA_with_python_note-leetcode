def inverted_right_angled_triangle(n):
    triangle = []
    
    for i in range(n,0,-1):
        triangle.append('*'*i)
    
    return triangle

print(inverted_right_angled_triangle(5))