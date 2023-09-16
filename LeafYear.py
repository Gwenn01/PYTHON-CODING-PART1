def leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print("leap year")
            else:
                print("not leap year")
        else:
            ptint("leap year")                     
    else:
        print("not leap year")
        
n = int(input('Input Year: '))
leap_year(n)     