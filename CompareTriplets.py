# if a[i] > b[i] add point, opposite, if equal just ignore comparing a[i] b[i]
def compare_triplets(a, b):
    a_points = 0
    b_points = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_points += 1
        if b[i] > a[i]:
            b_points += 1
    temp = []
    temp.append(a_points)
    temp.append(b_points)
    return temp
    
a = [17, 28, 30]
b = [99, 16, 8]
print(compare_triplets(a, b))