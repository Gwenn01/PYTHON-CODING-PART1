def factorialOfDigits(n):
    temp = n
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    result = 0
    while n > 0:
        rem = n % 10
        c = count 
        multiply = 1
        while c > 0:
            multiply *= rem
            c -= 1
        result += multiply
        n //= 10
    return result
                
n = 123
print(factorialOfDigits(n))