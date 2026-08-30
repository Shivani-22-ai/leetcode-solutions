class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi = nums.index(min(nums))
        ma = nums.index(max(nums))
        if mi == ma:
            return 1
        l = len(nums)
        ans = min(max(mi,ma)+1,l-(min(mi,ma)),(min(mi,ma)+1)+(l-max(mi,ma)))
        return ans
        