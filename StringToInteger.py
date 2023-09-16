#String to Integer
class Solution:
    def atoi(self, s):
        num = "1234567890"
        is_positive = True
        result = ""
        for i in range(len(s)):
            if s[i] 
            if s[i] in num:
                result += s[i]
            if s[i] == '-':
                is_positive = False            
        numbers = int(result)            
        if not is_positive:
           numbers = -abs(numbers)
        return numbers

solution = Solution()
print(solution.atoi("4232 is my words"))           