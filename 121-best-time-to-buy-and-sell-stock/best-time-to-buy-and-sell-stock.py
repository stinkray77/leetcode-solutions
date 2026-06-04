class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for i, val in enumerate(prices):
            if (prices[i] < buy):
                buy = prices[i]
            elif (prices[i] - buy > maxProfit):
                maxProfit = prices[i] - buy
            
        return maxProfit