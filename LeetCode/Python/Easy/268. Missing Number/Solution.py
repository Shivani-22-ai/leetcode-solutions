class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        t = (n*(n+1))//2
        actual = sum(nums)
        return (t-actual)

