class Solution:
    def reverse(self, x: int) -> int:
        # if its big number return 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if x >= INT_MAX or x <= INT_MIN:
            return 0
        # if negative convert to positive
        result = 0
        is_negative = False
        if x < 0:
            x = abs(x)
            is_negative = True
        while x != 0:
            rem = x % 10
            result = result * 10 + rem
            x //= 10
        # the convert again      
        if is_negative:
            result = -abs(result)
            
        if result >= INT_MAX or result <= INT_MIN:
            return 0  
                  
        return result

solution = Solution()
print(solution.reverse(1534236469))                     