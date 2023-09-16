class Solution:
    def reverse(self, string):
        # simple reversing string
        string = list(string)
        start = 0
        end = len(string)-1
        while start < end:
            temp = string[start]
            string[start] = string[end]
            string[end] = temp
            start += 1
            end -= 1
        result = ''.join(string)
        return result        
        
    def reverseBits(self, n):
        # Convert our binary into string and remove the '0b' prefix
        binary_string = bin(n)[2:]     
        # After reversing it
        reversed_binary_string = self.reverse(binary_string)    
        # Add the '0b' prefix back
        reversed_binary_string = "0b" + reversed_binary_string
        
        # Convert it again into a number
        number = int(reversed_binary_string, 2)
        return number
        
solution = Solution()
n = 0b00000010100101000001111010011100
ans = solution.reverseBits(n) 
print(ans)     