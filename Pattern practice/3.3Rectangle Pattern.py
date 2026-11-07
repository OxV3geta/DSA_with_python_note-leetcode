def Rectangle_Pattern(n,m):
    
    rectanle = []
    
    for i in range(n):
        row = '*' * m
        rectanle.append(row)
        
    return rectanle
        
        

print(Rectangle_Pattern(4,5))