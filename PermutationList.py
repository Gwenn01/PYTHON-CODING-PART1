class Solution:
     def permutation(self, process, nums, index, list_result):
        # base condition
        if index == len(nums):
            list_result.append(process)
            return
        # iterate the len of process
        ch = nums[index]
        for i in range(len(process)+1):
            first = process[0 : i]
            second = process[i : len(process)]
            concat = first + [ch] + second
            #recursion call
            self.permutation(concat, nums, index + 1, list_result)
            
     def permute(self, nums):
        list_result = []
        self.permutation([], nums, 0, list_result)
        return list_result
        
 
solution = Solution()
nums = [0, -1, 1]
ans = solution.permute(nums)
print(ans)