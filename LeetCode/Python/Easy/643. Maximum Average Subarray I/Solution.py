class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s+=nums[i]
        mx = s/k 

        for r in range(k,len(nums)):
            s+=nums[r]
            s-=nums[r-k]
            mx = max(mx,s/k)
        return mx

        


        