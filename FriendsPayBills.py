import random

names = input('Enter friends name: ')
list = names.split()
index = random.randint(0, len(list)-1)

print(f"{list[index]} ganna pay the bills")
