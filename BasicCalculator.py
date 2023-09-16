def add(x, y):
    return x + y
 
def subtract(x, y):
    return x - y
   
def multiply(x, y):
    return x * y
 
def divide(x, y):
    return x / y
    
first_num = int(input("Enter second number: "))
second_num = int(input("Enter second number: "))
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
op = int(input("Enter operator: "))

if op == 1:
    x = add(first_num, second_num)
    print(x)
    
elif op == 2:
    x = subtract(first_num, second_num)
    print(x)
    
elif op == 3:
    x = multiply(first_num, second_num)
    print(x)
    
elif op == 4:
    x = divide(first_num, second_num)
    print(x)
    
else:
    print("Invalid Operator")