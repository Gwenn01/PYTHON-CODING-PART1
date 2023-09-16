class Solutions:
    def single_number(self, nums):
        nums.sort()
        for i in range(0, len(nums)-1, + 2):
            if nums[i] != nums[i+1]:
                return nums[i]
            
        return nums[len(nums)-1]
            
        
solution = Solutions()
nums = [1, 2, 2]
ans = solution.single_number(nums)
print(ans)