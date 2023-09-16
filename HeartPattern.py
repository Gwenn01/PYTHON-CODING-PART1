length = int(input("Enter Length: "))
# print the two increament 
for i in range(1, length+1):
    for j in range((length+1)-i):
        print(" ", end="")
    for j in range(1, (i*2)+1):
        print("*", end="")
    for j in range((length)-i):
        print("  ", end="")
    for j in range(1, (i*2)+1):
        print("*", end="") 
    print()    
# print the V shape
for i in range(1, (length+1)* 2):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(1, ((length+1)*2)-i):
        print("*", end="")
    for j in range(1, ((length+1)*2)-i):
        print("*", end="")      
    print()                              