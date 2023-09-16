def reversal(s):
    return helper(s, 0)
    
def helper(s, i):
    if i == len(s)-1:
        return s[i]
    return helper(s, i + 1) + s[i]
    
s = reversal("hello world")
print(s)