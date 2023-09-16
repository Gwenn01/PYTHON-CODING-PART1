# bubble Sort
def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(1, len(my_list)-i):
            if my_list[j-1] > my_list[j]:
                temp = my_list[j-1]
                my_list[j-1] = my_list[j]
                my_list[j] = temp
    return my_list                
my_list = [5, 2, 9, 1, 7, 10]
print(bubble_sort(my_list))