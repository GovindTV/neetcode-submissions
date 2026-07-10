class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, mini,profit = 1, prices[0],0
        while i < len(prices):
            profit = max(profit, prices[i] - mini,0)
            mini = min(mini,prices[i])
            i += 1
        return profit