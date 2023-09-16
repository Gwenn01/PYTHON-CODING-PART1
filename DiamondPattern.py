length = int(input("Enter length: "))
# increament pettern
for i in range(length):
    for j in range(length-i):
        print(" ", end="")
    for j in range(-1, i):
        print("*", end="")
    for j in range(0, i):
        print("*", end="")
    print()
# decrement pettern
for i in range(length):
    for j in range(-1, i):
        print(" ", end="")
    for j in range(length-i):
        print("*", end="")
    for j in range(1, length-i):
        print("*", end="")
    print()