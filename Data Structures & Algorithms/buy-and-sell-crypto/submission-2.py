class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestBeforeI = max(prices)
        for i, price in enumerate(prices):
            maxProfit = max(maxProfit, price - lowestBeforeI)

            lowestBeforeI = min(price, lowestBeforeI)
        return maxProfit
