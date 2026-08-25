class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}    
        for i in range(0,len(nums)):
            com = target - nums[i]
            if com in hm:
                return [i,hm[com]]
            hm[nums[i]] = i

         


            
        