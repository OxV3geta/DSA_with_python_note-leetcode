def right_angled_triangle(n):
    
    triangle = []
    
    for i in range(1,n+1):
        triangle.append('*'*i)
        
        
    return triangle

print(right_angled_triangle(5))