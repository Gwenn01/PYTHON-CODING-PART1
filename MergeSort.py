#Merge Sort
#copy of range
def copy_range(my_list, start, end):
    temp = []
    for i in range(start, end):
            temp.append(my_list[i])
    return temp

# merging
def merging(left, right):
    temp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
            
    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
       temp.append(right[j])
       j += 1
    
    return temp
                 
#merge calling recursion    
def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
   #get mid to half the list     
    mid = len(my_list) // 2
    # left range
    temp_left = copy_range(my_list, 0, mid)
    # recursion call
    left = merge_sort(temp_left)
    # right range
    temp_right = copy_range(my_list, mid, len(my_list))
    #recursion call
    right = merge_sort(temp_right)
    
    return merging(left, right)    

# Calling function         
my_list = [28, 13, 5, 9, 21, 16, 19, 2, 3]
print(merge_sort(my_list)) 
   