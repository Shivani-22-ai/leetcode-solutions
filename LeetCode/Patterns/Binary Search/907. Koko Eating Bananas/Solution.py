import math
def canEat(piles,h,mid):
    hours = 0
    for i in piles:
        hours += math.ceil(i/mid)
    return hours <= h

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        while(l<=r):
            mid = l +(r-l)//2
            if canEat(piles,h,mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans