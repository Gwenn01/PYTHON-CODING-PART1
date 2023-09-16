def sumOfDigits(n):
    while n > 9:
        sum = 0
        while n != 0:
            rem = n % 10
            sum += rem
            n //= 10
        n = sum
    return n

print(sumOfDigits(15))    