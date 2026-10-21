class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mine = prices[0]
        maxp = 0
        for i in range(1,len(prices)):
            mine = min(prices[i],mine)
            maxp = max(maxp,prices[i]-mine)
        return maxp


        
        
        