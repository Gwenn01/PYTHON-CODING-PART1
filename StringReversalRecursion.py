# string reversal using adding the last
def reversal(p, s, i):
    #return if we reach the start
    if i ==  - len(s):
        p += s[i]
        return p
    
    return reversal(p + s[i], s, i - 1)
    
print(reversal("", "hello", -1))
    