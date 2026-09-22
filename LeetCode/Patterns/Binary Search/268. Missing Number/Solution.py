class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        act_sum = ((len(nums))*(len(nums)+1))//2
        real_sum = sum(nums)
        return act_sum - real_sum