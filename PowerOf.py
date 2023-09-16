def power_of(n1, n2):
    result = 1
    for i in range(n2):
        result *= n1
    return result      
 
print(power_of(5, 5))        