class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        cb = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if abs(s-target) < abs(cb-target):
                    cb = s
                if s == target:
                    return s
                if s>target:
                    k-=1
                else:
                    j+=1
        return cb

        