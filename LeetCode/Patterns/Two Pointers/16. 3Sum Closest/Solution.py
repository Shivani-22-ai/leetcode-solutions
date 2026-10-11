class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        cb = float('inf')
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if abs(s-target) < abs(cb-target):
                    cb = s
                if s>target:
                    k-=1
                else:
                    j+=1
        return cb

        