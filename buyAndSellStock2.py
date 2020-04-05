class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0: return 0
       
        profit_sum =0
        for i in range(1, len(prices)):
            print(prices[i]-prices[i-1])
            profit_sum += max(prices[i] - prices[i-1], 0)
        return profit_sum
