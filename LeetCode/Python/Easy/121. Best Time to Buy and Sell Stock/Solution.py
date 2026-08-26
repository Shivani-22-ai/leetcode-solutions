class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        maxp = 0
        for i in range(1,len(prices)):
            least = min(least,prices[i])
            maxp = max(maxp,prices[i]-least)
        return maxp

        
        
        