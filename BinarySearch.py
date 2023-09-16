# Binary Search
def binary_search(my_list):
    start = 0
    end = len(my_list) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target < my_list[mid]:
            start = start
            end = mid - 1
        elif target > my_list[mid]:
             start = mid + 1
             end = end
        else:
             return mid     
    
    return -1
    
    
my_list = [2, 5, 7, 10, 15, 17, 20]
target = 5
print(binary_search(my_list))
