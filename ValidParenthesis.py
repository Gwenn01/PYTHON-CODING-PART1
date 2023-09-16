def is_valid(s):
    s = list(s)
    stack = []
    for i in range(len(s)):
        # add all the open parenthe
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        else:
             if not stack:
                 return False
          # check if close is equal to open 
             temp = stack.pop()
             if s[i] == ')':
                 if temp != '(':
                     return False
             elif s[i] == ']':
                  if temp != '[':
                     return False
             elif s[i] == '}':
                  if temp != '{':
                     return False
    return True            
          
s = "(()[]{})" 
print(is_valid(s))         