class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        def compute_profit(i , j):
            return prices[j] - prices[i]
        for i in range(len(prices)):
            for j in range(i + 1 , len(prices)):
                if prices[j] > prices[i]:
                    max_profit = max(compute_profit(i , j) , max_profit)
        return max_profit
