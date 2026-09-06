class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        mxa = float('-inf')
        for i in range(k):
            s+=nums[i]
        mxa = max(mxa,s/k)
        l=0
        r=k
        while(r<len(nums)):
            s-=nums[l]
            l+=1
            s+=nums[r]
            mxa = max(mxa,s/k)
            r+=1
        return mxa
        


        