def reverse(str, start, end):
    while start < end:
        temp = str[start]
        str[start] = str[end]
        str[end] = temp
        start += 1
        end -=1

def reverse_each(str):
    convert_list = list(str)
    start = 0
    end = 0
    # iterate througj str
    for i in range(len(convert_list)):
        if convert_list[i] == " ":
            # set pointers to reverse
            end = i-1
            reverse(convert_list, start, end)
            start = i+1
    result = ""
    #convert list into string
    for listt in convert_list:
        result += listt
    return result
 
#call the main function
str = "My name is Hello World"
ans = reverse_each(str)
print(ans)
