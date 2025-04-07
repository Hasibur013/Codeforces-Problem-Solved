t = int(input())
while t>0:
    # m = int(input())
    # a = int(input())
    # b = int(input())
    # c = int(input())
    m, a, b, c = map(int, input().split())
    
    result = 0
    a_space = 0
    b_space = 0
    
    
    if a <= m:
        result += a
        a_space = m - a
    else:
        result += m
        
    if b <= m:
        result += b
        b_space = m - b
    else:
        result += m
        
        
    if c <= a_space + b_space:
        result += c
    else:
        result += a_space + b_space
        
    print(result)
        
    t -=1
    

