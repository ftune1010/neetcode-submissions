class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        high=low=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<low:
                high=low=prices[i]
            elif prices[i]>high:
                high=prices[i]
                profit=max(profit,high-low)
        return profit
        