class Solution:
    def divide(self, dividend, divisor):
        # base condition
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend 
        # check if its negative
        is_negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            is_negative = True
        # convert it into positive
        # so we can subtract
        c_dividend = abs(dividend)
        c_divisor = abs(divisor)
        # subtract till zero and count ans
        answer = 0
        while c_dividend  >= c_divisor:
            answer += 1
            c_dividend -= c_divisor
        
        if is_negative:
            return -abs(answer)
        return answer
        
# call our method
solution = Solution()      
dividend = -7
divisor = -2
ans = solution.divide(dividend, divisor)
print(ans)
