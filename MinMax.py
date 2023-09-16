arr = [10, 5, 17, 3, 8, 9, 12]
min = 10000000
max = 0
print(arr)

for ar in arr:
    if ar > max:
        max = ar
    if ar < min:
        min = ar
print(f"Max: {max}")
print(f"Min: {min}")