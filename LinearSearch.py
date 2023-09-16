#Linear Search
def linear_search(my_list):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1            

my_list = [2, 6, 10, 5, 2, 1]
target = 5
print(linear_search(my_list))