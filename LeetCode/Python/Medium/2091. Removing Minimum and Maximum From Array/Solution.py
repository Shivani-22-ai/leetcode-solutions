class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi = nums.index(min(nums))
        ma = nums.index(max(nums))
        if mi == ma:
            return 1
        l = len(nums)
        front = 0
        rear = 0
        if mi+1 <= l-mi:
            minr = mi+1
            front = 1
        else:
            minr = l-mi
            rear = 1  
        if ma+1 <= l-ma:
            maxr = ma+1
            front+=1
        else:
            maxr = l-ma
            rear+=1
        
        if front == 2:
            return max(minr,maxr)
        if rear == 2:
            return max(minr,maxr)
        else:
            return maxr+minr
        
        