def remove(s):
    result = ""
    for i in range(1, len(s)):
        #check first and sencond in S
        if s[i-1] != s[i]:
                result += s[i-1]
            #if we are in end, and its not equal to the prev then add it
        if i == len(s)-1:
                    result += s[i]                       
    return result
                    
s = "aaabbbccdeeef"
print(remove(s))