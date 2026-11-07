def gen_squre(n):
    squre = []
    
    for i in range(0,n):
        squre.append('*' * n)
    
    return squre

print(gen_squre(2))