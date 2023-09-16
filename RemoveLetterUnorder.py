class Solution:
    def remove(self, s):
        convert = list(s)
        # all duplicates convert to " "
        for i in range(len(convert)):
            for j in range(i+1, len(convert)):
                # base condition
                if convert[i] == " ":
                    break
                if convert[i] == convert[j]:
                    convert[j] = " "
         # add only the letter
        result = ""       
        for i in convert:
            if i != " ":
                result += i
        return result
                        
s = Solution()
print(s.remove("bcabc"))                                