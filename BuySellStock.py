class Solutions:
    def max_profit(self, prices):
        maxProfit = 0
        # left is to buy
        left = 0
        # right is to sell
        right = len(prices)-1
        while(left < right):
            if prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                if temp > maxProfit:
                    maxProfit = temp
                right -= 1
            else:
                left += 1
        return maxProfit
        
                
solution = Solutions()
#prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
ans = solution.max_profit(prices)   
print(ans)         