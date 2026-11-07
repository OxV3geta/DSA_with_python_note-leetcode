
def hollow_Square_of_side(n):
    squre = []
    
    if n == 1:
        return ['*']
        
    squre.append('*'*n)

    for num in range(n-2):
        squre.append('*' + ' ' * (n-2) + '*')
    
    squre.append('*'*n)
    
    return squre
print(hollow_Square_of_side(5))

