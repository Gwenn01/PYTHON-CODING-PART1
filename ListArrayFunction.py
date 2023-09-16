# list = [] turple = ()
# the main dif is turple is constant
# return the length
def len(my_list):
    length = 0
    for item in my_list:
        length += 1        
    return length
# count a give value 
def count(my_list, value):
    count = 0
    for item in my_list:
        if item == value:
            count += 1       
    return count
# add element in the end
def append(my_list, value):
    index = len(my_list)-1
    my_list[index] = value
# insert element in particular index
def insert(my_list, index, value):
    temp = []
    i = 0
    j = 0
    for j in range(len(my_list)+1):
        if j == index:
            temp.append(value)
        else:
            temp.append(my_list[i])
            i += 1            
    my_list[:] = temp
 # remove element i particular value   
def remove(my_list, value):
    temp = []
    i = 0
    for i in range(len(my_list)):
        if my_list[i] != value:
            temp.append(my_list[i])
    my_list[:] = temp
# remove element in given index
def pop_index(my_list, index):
    temp = []
    i = 0
    for i in range(len(my_list)):
        if i != index:
            temp.append(my_list[i])
    my_list[:] = temp
# remove element in the end
def pop(my_list):
    temp = []
    i = 0
    for i in range(len(my_list)-1):
            temp.append(my_list[i])
    my_list[:] = temp
# delete all element    
def dele_all(my_list):
     my_list[:] = []
# delete element in give index     
def dele(my_list, index):
    temp = []
    i = 0
    for i in range(len(my_list)):
        if i != index:
            temp.append(my_list[i])
    my_list[:] = temp
# clear all element
def clear(my_list):
    my_list[:] = []       
# copy list in new list
def copy(my_list):
    temp = []
    for i in range(len(my_list)):
        temp.append(my_list[i])       
    return temp
# extend a list
def extend(my_list, extend_list):
    temp = []
    for i in range(len(my_list)):
        temp.append(my_list[i])
    for j in range(len(extend_list)):
        temp.append(extend_list[j])
    my_list[:] = temp
# reverse list
def reverse(my_list):
    temp = []
    # range(length, to, decreament)
    for i in range((len(my_list)-1), -1, -1):
         temp.append(my_list[i])           
    my_list[:] = temp
# sort list
def sort(my_list):
    for i in range(0, (len(my_list))):
        for j in range(1, (len(my_list)-i)):
            if my_list[j] < my_list[j-1]:
                temp = my_list[j-1]
                my_list[j-1] = my_list[j]
                my_list[j] = temp
# to string
def to_string(my_list):
    result = ""
    result += "["
    for i in range(len(my_list)):
        result += str(my_list[i])
        if i != len(my_list)-1:
            result += ", "
    result += "]"
    return result
    
my_list = [5, 3, 1, 4, 2]
print(to_string(my_list))