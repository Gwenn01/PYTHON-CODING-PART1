class Solution:
    def numberOfBits(self, n):
        count = 0
        # convert binary into string
        binary_string = bin(n)[2:]
        # then count it
        for s in binary_string:
            if s == '1':
                count += 1
        return count
        
solution = Solution()
n = 0b0000000000001010100101001
ans = solution.numberOfBits(n)
print(ans)        