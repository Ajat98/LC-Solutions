'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
             '''
             
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        #ineffecient solution with large list values
        if prices == sorted(prices, reverse=True,):
            return 0

        p = []
        for i in prices:
            #k will be day stock is sold, i is day price is bought at
            for k in prices[prices.index(i):]:
                profit = k - i
                p.append(profit)
        return max(p)
        '''
        
        buy_p = float('inf')
        profit = 0
        
        for p in prices:
            if p < buy_p:
                buy_p = p
            if p - buy_p > profit:
                profit = p - buy_p
        return profit
             
