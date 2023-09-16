def split_pairs(s):
    result = []
    #if len is odd, then it remain 1 letter 
    if len(s) % 2 != 0:
        s += "_"
    #add in list per 2    
    for i in range(0, len(s), 2):
        result.append(s[i : i+2])
        
    return result
        
print(split_pairs("abcdefg"))        