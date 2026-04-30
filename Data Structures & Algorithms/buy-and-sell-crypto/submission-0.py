class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float('inf')

        for n in prices:
            lowest = min(lowest, n)
            profit = max(n - lowest, profit)

        return profit
