class Solution:
    def median_arr(self, num1, num2):
        # first merge the two array
        merged = self.merge(num1, num2)
        # get the mid 
        mid = len(merged) // 2
        # if len is even, return mid num
        if len(merged) % 2 == 1:
            return float(merged[mid])
        else:
            s_mid = mid -1
            e_mid = mid
            ans = (merged[s_mid] + merged[e_mid]) / 2
            return ans
            
   # merge the two array         
    def merge(self, num1, num2):
        temp = []
        i = 0
        j = 0
        # merge two num
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                temp.append(num1[i])
                i += 1
            else:
                temp.append(num2[j])
                j += 1
        while i < len(num1):
            temp.append(num1[i])
            i += 1
        while j < len(num2):
            temp.append(num2[j])
            j += 1
            
        return temp

# call the method     
solution = Solution()
num1 = [1, 2]
num2 = [3, 4]
ans = solution.median_arr(num1, num2)
print(ans)        