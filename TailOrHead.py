import random

ran = random.randint(0, 1)
user = int(input('Head or Tail: (0/1): '))
if ran == 0:
    print("Its a Head")
else:
    print("Its a Tail")
    
if user == ran: 
    print("You Win")
else:
    print("You Lose")