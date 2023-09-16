def remainder(n1, n2):
    if n2 > n1: return n2 - n1    
    while n1 >= n2:
        n1 -= n2
    return n1

n1 = 5
n2 = 2
print(remainder(n1, n2))        