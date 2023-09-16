class Solution:
    def combi_sum(self, array, container, ListofList, target):
        # sum it first to compare in target
        sum = 0
        for i in range(len(container)):
            sum += container[i]
        # base condition
        if sum > target:
            return
        # if we find a ans, then add it
        if sum == target:
            ListofList.append(container.copy())
            return
        # call the recursion
        for arr in array:
            container.append(arr)
            self.combi_sum(array, container, ListofList, target)
            # then backtrack if we did not find the answer
            container.pop()
                    
    def combinationSum(self, candidates, target):
        ListofList = []
        container = []
        self.combi_sum(candidates, container, ListofList, target)
        # remove the duplicated ans
        unique_combinations = set(tuple(sorted(lst)) for lst in ListofList)
        ListofList = [list(comb) for comb in unique_combinations]
        
        return ListofList
        
                
              
solution = Solution()
candidates = [2, 3, 5]       
target = 8   
ans = solution.combinationSum(candidates, target)
print(ans)