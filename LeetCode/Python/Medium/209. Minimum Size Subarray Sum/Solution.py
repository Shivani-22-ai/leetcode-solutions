class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        ans = float('inf')
        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                ans = min(ans,r-l+1)
                window_sum -= nums[l]
                l+=1
                
        if ans == float('inf'):
            return 0 
        else:
            return ans
        