import math
def canDiv(nums,threshold,mid):
    s = 0
    for i in nums:
        s += math.ceil(i/mid)
    return s<=threshold

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        l = 1
        h = max(nums)
        ans = 0
        while l<=h:
            mid = l + (h-l)//2
            if canDiv(nums,threshold,mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans

        