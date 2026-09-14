class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        ma = nums[0]
        for r in range(1,len(nums)):
            s = max(nums[r] , s+nums[r])
            ma = max(s,ma) 
        return ma