def Pyramid_Pattern(n):
    pyramid = []
    
    for i in range(1, n + 1)[::-1]:
        stars = '*' * (2 * i - 1)
        # also we can use this formula for reverse "stars = '*' * (2 * (n - i + 1) - 1)
        
        spaces = ' ' * (n - i)
    
        pyramid.append(spaces + stars + spaces)
    
    return pyramid

print(Pyramid_Pattern(6))