def first_non_dup(s):
    count = 0
    result = ""
    for i in range(1,len(s)):
        #count the equal or duplicate
        if s[i-1] == s[i]:
            count += 1
        else:
            #if count is 0 the return 
            if count == 0:
                return s[i-1]
            #reset the count for other letter
            count = 0
        # check the last char of S 
        if i == len(s)-1:
            if count == 0:
                return s[i]
     # return no if all is dup  
    return None 
               
s = "aaabbbcccdde"
print(first_non_dup(s))       