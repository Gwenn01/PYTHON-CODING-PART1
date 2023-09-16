# Insertion Sort
def insertion_sort(my_list):
    for i in range(0, len(my_list)-1, +1):
        for j in range(i+1, 0, -1):
            if my_list[j] < my_list[j-1]:
                temp = my_list[j]
                my_list[j] = my_list[j-1]
                my_list[j-1] = temp
            else:
                break
    return my_list        
                    
my_list = [5, 8, 2, 4, 1, 10, 15]
print(insertion_sort(my_list))
