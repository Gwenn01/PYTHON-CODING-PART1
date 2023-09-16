class Solution:    
    def remove(self, s):
        s = self.sort(s)
        result = ""
        for i in range(1, len(s)):
            #check first and sencond in S
            if s[i-1] != s[i]:
                    result += s[i-1]
                #if we are in end, and its not equal to the prev then add it
            if i == len(s)-1:
                    result += s[i]                       
        return result
    # sort the string to easily remove
    def sort(self, s):
        temp_list = list(s)
        for i in range(len(temp_list)):
            for j in range(1, len(temp_list)-i):
                if temp_list[j] < temp_list[j-1]:
                    temp = temp_list[j]
                    temp_list[j] = temp_list[j-1]
                    temp_list[j-1] = temp
        result = "".join(temp_list)                
        return result

solution = Solution()
s = "bacdbab"
ans = solution.remove(s)
print(ans)
                                    