def floyds_triangle(n):
    
    triangle = []
    current_num = 1
    
    for i in range(1,n+1):
        row = []
        for j in range(i):
            row.append(str(current_num))
            current_num += 1
            
        triangle.append((row))        
    return triangle
    
print(floyds_triangle(4))
