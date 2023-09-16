def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{j*i}  ", end="")
        print()
          
multiplication_table()