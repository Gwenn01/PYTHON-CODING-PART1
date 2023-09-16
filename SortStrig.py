def sort(s):
    temp_list = list(s)
    for i in range(len(temp_list)):
        for j in range(1, len(temp_list)-i):
            if temp_list[j] < temp_list[j-1]:
                temp = temp_list[j]
                temp_list[j] = temp_list[j-1]
                temp_list[j-1] = temp
    result = "".join(temp_list)                
    return result            
                
s = "bacbd"
s = sort(s)
print(s)