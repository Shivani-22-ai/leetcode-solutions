class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n+1):
            ans ^= i
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
