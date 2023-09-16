def pizza_order():
    totalBill = 0
    print("1. Small Pizza 100")
    print("2. Medium Pizza 200")
    print("3. Large Pizza 300")
    op = int(input("Enter Size: "))
    if op == 1:
        totalBill = 100
        pepperoni = input("Do you want to add pepperoni? (y/n)")
        if pepperoni == 'y':
            totalBill += 30
        cheese = input("Do you want to add cheese? (y/n)")
        if pepperoni == 'y':
            totalBill += 20       
    elif op == 2:
        totalBill = 200
        pepperoni = input("Do you want to add pepperoni? (y/n)")
        if pepperoni == 'y':
            totalBill +=50
        cheese = input("Do you want to add cheese? (y/n)")
        if pepperoni == 'y':
            totalBill += 20     
    elif op == 3:
        totalBill = 300
        pepperoni = input("Do you want to add pepperoni? (y/n)")
        if pepperoni == 'y':
            totalBill += 50
        cheese = input("Do you want to add cheese? (y/n)")
        if pepperoni == 'y':
            totalBill += 20     
    else:
         print("Invalid")
                
    print(f"Total Bill: {totalBill}")                      
pizza_order()    