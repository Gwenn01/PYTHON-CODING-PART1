class Solutions:
    #removing the non-alpha & lower it
    def converting(self, s):
        s = s.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        result = ""
        for i in s:
            for j in alpha:
                if i == j:
                    result += i
                    break
        return result
   # reverse it     
    def reverse(self, s):
        s = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        result = ''.join(s)
        return result
                                     
    def valid_palindrome(self, s):
        if s == " ":
            return True
        s = self.converting(s)
        r = self.reverse(s)
        return s == r
        
        
        
solution = Solutions()
#s = "A man, a plan, a canal: Panama"
s = "0P"
ans = solution.valid_palindrome(s)
print(ans)