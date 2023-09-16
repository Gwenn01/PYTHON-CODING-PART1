class Solution:    
    def reverse(self, s, k):
        # base condition
        if len(s) == 1 or k == 1: return s
        s = list(s)
        # if k >= s length reverse all
        if k >= len(s)-1:
            start = 0
            end = len(s)-1
            while start < end:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1
            return ''.join(s) 
         # reverse in k length
        for i in range(0, len(s)-1, k+k):
            start = i
            end = (i+k) - 1
            while start < end:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1
        return ''.join(s)

solu = Solution()    
s = "ba"    
k = 1
print(solu.reverse(s, k))            