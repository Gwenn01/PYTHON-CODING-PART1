class Solution:
    # convert the srt binary into numeric value so that we can sum in then convert ut again to numeric after adding it
    def convert_numeric(self, str):
        result = 0
        n = len(str) - 1
        multiply = 1
        for i in range(n, -1, -1):
            if str[i] == '1':
                result += multiply
            multiply *= 2
        return result
    
    def convert_binary(selft, num):
        result = ""
        while num > 0:
            if num % 2 == 1:
                result = '1' + result
            else:
                result = '0' + result
            num = num // 2
        if result == "":
            return "0"
        return result
                
        
    def add_binary(self, a, b):
        num1 = self.convert_numeric(a)
        num2 = self.convert_numeric(b)
        sum = num1 + num2
        return self.convert_binary(sum)
    
        

# call the main function
solution = Solution()
a = "1010"
b = "1011"
print(solution.add_binary(a, b))        