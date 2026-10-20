class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        m = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == m:
                c+=1
            else:
                c-=1
            if c == 0:
                m = nums[i]
                c+=1
        return m
            
        


        