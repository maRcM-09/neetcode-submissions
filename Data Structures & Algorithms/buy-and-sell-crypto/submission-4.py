class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0
        R = 1
        def compute_profit(i , j):
            return prices[j] - prices[i]
        n = len(prices)
        while R < n:
            if prices[L] < prices[R]:
                max_profit = max(compute_profit(L,R),max_profit)
            else:
                L=R
            R+=1

        return max_profit
