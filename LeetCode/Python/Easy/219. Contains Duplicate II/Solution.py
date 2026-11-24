class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                if abs(hm[nums[i]]-i) <= k:
                    return True
            hm[nums[i]] = i
        return False   
                 
        

        