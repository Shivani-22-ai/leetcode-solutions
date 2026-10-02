def canEat(piles,h,mid):
    hours = 0
    for p in piles:
        hours += ceil(p/mid)
    return hours<=h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        high = max(piles)
        while(l<=high):
            mid = l+(high-l)//2
            if canEat(piles,h,mid):
                ans = mid
                high = mid - 1
            else:
                l = mid + 1
        return ans
        