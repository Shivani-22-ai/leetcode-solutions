class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hm = {-1:0}
        for i in range(len(nums)):
            if nums[i] in hm:
                prev = hm[nums[i]]
                if abs(prev-i) <= k:
                    return True
                hm[nums[i]] = i
            hm[nums[i]] = i
        return False   
                 
        

        