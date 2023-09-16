#cyclic Sort
def cyclic_sort(my_list):
    i = 0
    while i < len(my_list):
        # get the correct position
        correct_index = my_list[i] - 1
        # if not in correct position, swap
        if correct_index < len(my_list) and my_list[correct_index] != my_list[i]:
            temp = my_list[correct_index]
            my_list[correct_index] = my_list[i]
            my_list[i] = temp
        # if correct just keep moving       
        else:
            i += 1        
    return my_list
        
my_list = [5, 4, 1, 3, 2]
print(cyclic_sort(my_list))    