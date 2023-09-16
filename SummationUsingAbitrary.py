def summation(*num):
    sum = 0
    for i in num:
        sum += i
    return sum
        
n = summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
print(n)
