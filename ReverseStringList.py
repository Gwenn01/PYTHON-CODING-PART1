def reverse(s):
    start = 0
    end = len(s)-1
    
    while start < end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1

s = ["h", "e", "l", "l", "o"]
print("Original: ", s)
reverse(s)
print("Reverse: ", s)