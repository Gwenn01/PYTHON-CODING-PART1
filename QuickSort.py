# Quick Sort
def quick_sort(my_list, upper_bound, lower_bound):
    # base condition
    if upper_bound >= lower_bound:
        return
    # initialize out indexes
    start = upper_bound
    end = lower_bound
    mid = (start + end) // 2
   # pivot to compare the start and end
    pivot = my_list[mid]
    while start <= end:
        # if less ir greater then move
        while my_list[start] < pivot:
            start += 1
        while my_list[end] > pivot:
            end -= 1
         # if loops stop then swap end and start
        if start <= end:
             temp = my_list[start]
             my_list[start] = my_list[end]
             my_list[end] = temp
             start += 1
             end -= 1
    
    # call the recursion
    quick_sort(my_list, upper_bound, end)
    quick_sort(my_list, start, lower_bound)


my_list = [3, 10, 1, 15, 9, 4, 8, 5, 7, 0]
quick_sort(my_list, 0, len(my_list)-1)
print(my_list)
