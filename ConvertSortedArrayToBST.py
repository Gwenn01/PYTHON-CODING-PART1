class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def __init__(self):
         self.root = None
    # solutions 
    def func_helper(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = self.TreeNode(nums[mid])
        node.left = self.func_helper(nums, left, mid - 1)
        node.right = self.func_helper(nums, mid+1, right)       
        return node        
        
    def sortedArray_toBST(self, nums):
        self.root = self.func_helper(nums, 0, len(nums)-1)
        
    # displaying the value
    def display(self):
        current = self.root
        detail = "Root Node: "
        self.display_temp(current, detail)
        
    def display_temp(self, node, detail):
         if node == None:
             return
         print(f"{detail}: {node.val}")
         self.display_temp(node.left, f"Left child of {node.val}: ")
         self.display_temp(node.right, f"Right child of {node.val}: ")  
                
# main method
solution = Solution()
nums = [-10, - 3, 0, 5, 9]
solution.sortedArray_toBST(nums)
solution.display()

        
        
        