# add digits using type casting
def add_digits_type(num):
    sum = 0
    digits = str(num)
    for i in range(len(digits)):
         sum += int(digits[i])
    return sum
# add digits using remainder
def add_digits_remain(num):
   sum = 0
   while num != 0:
       rem = num % 10
       sum += rem
       num //= 10
   return sum       
   
num = int(input('Enter a number: '))
print(add_digits_remain(num))   