# Selection sort
def selection_sort(my_list):
    length = len(my_list)-1
    for i in range(len(my_list)):
        max = 0
        for j in range(1, len(my_list)-i, +1):
            # get max
            if my_list[j] > my_list[max]:
                max = j
        # put in the end
        temp = my_list[length-i]
        my_list[length-i] = my_list[max]
        my_list[max] = temp
    return my_list
        
my_list = [7, 5, 1, 2, 4, 9, 15, 10, 3]
print(selection_sort(my_list))
