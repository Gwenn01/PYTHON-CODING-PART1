def sum(n):
    if n == 1:
        return n
    
    return n + sum(n-1)

print(sum(10))