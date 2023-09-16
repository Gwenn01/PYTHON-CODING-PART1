class Solution:
    # main method
    def generate_parenthesis(self, n):
        # container to store ans
        result = []
        self.generate(n, 0, 0, "", result)
        return result
        
    # check if its valid parenthesis     
    def is_valid(self, p):
        stack = []
        for i in range(len(p)):
            if p[i] == '(' or p[i] == '{' or p[i] == '[':
                stack.append(p[i])
            else:
                # if empty just return 
                # to avoid error
                if not stack:
                    return False
                stack_temp = stack.pop()
                if p[i] == ')':
                    if stack_temp != '(':
                        return False
                elif p[i] == '}':
                    if stack_temp != '{':
                        return False
                elif p[i] == ']':
                    if stack_temp != '[':
                        return False
        return True
    
    # generste perenthesis 
    def generate(self, n, start, end, p, result):
        # base condition
        if start == n and end == n:
            if self.is_valid(p):
                result.append(p)
            return
        # call the recursion
        if start < n:
            self.generate(n, start + 1, end, p + '(', result)
        if end < n:
            self.generate(n, start, end + 1, p + ')', result)
            

                    
# call the function
solution = Solution()
ans = solution.generate_parenthesis(3)
print(ans)