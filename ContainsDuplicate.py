class Solution:
    def contains_duplicate(self, nums):
        if len(nums) <= 1:
            return False            
        nums.sort()
        for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    return True
                
        return False

s = Solution()    
nums = [1, 2, 3, 4, 5, 1]
print(s.contains_duplicate(nums))           