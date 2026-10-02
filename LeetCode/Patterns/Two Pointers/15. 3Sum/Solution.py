class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                continue
            a = nums[i]
            p1 = i+1
            p2 = n-1
            while(p1<p2):
                b = nums[p1]
                c = nums[p2]
                if a+b+c == 0:
                    l.append([a,b,c])
                    p1+=1
                    p2-=1
                    while p1<p2 and nums[p1] == nums[p1-1]:
                        p1+=1
                    while p1<p2 and nums[p2] == nums[p2+1]:
                        p2-=1
                elif a+b+c < 0:
                    p1+=1
                else:
                    p2-=1
        return l
        

        