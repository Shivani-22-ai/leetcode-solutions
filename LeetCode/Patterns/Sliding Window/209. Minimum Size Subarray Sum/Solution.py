class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wis = 0
        ans = float('inf')
        l = 0
        for r in range(len(nums)):
            wis += nums[r]
            while l<=r and wis>=target:
                ans = min(ans,r-l+1)
                wis -= nums[l]
                l+=1
        if ans == float('inf'):
            return 0
        return ans           
